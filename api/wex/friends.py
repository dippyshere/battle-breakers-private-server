"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the wex friends service
"""
import urllib.parse

import sanic

from utils import types
from utils.exceptions import errors
from utils.friend_system import PlayerFriends
from utils.profile_system import PlayerProfile
from utils.enums import ProfileType
from utils.sanic_gzip import Compress
from utils.utils import search_for_display_name

compress = Compress()
wex_friend = sanic.Blueprint("wex_friend")


# undocumented
@wex_friend.route("/api/game/v2/friends/<accountId>/search", methods=['GET'])
@compress.compress()
async def wex_friends_search(request: types.BBRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to search for friends
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    account_ids = []
    results = []
    display_name = urllib.parse.unquote(request.args.get("name", ""))
    # we treat this as not found instead of bad request, so that the client will show "0 results" instead of
    # popping up an error
    if not display_name:
        raise errors.com.epicgames.world_explorers.not_found(errorMessage="Missing required query parameter: name")
    if display_name == "":
        raise errors.com.epicgames.world_explorers.not_found(errorMessage="Missing required query parameter: name")
    search_results = await search_for_display_name(request.app.ctx.db, display_name)
    if search_results:
        account_ids.extend(search_results)
    if accountId in account_ids:
        account_ids.remove(accountId)
    # TODO: investigate incoming / outgoing friend requests in search results
    if accountId not in request.app.ctx.friends:
        request.app.ctx.friends[accountId] = await PlayerFriends.init_friends(accountId)
    for friend in request.app.ctx.friends[accountId].friends["friends"]:
        if friend["accountId"] in account_ids:
            account_ids.remove(friend["accountId"])
    for account_id in account_ids:
        account_data: dict = await request.app.ctx.db["accounts"].find_one({"_id": account_id}, {
            "displayName": 1,
        })
        if account_id not in request.app.ctx.profiles:
            request.app.ctx.profiles[account_id] = await PlayerProfile.init_profile(account_id)
        wex_data = await request.app.ctx.profiles[account_id].get_profile(ProfileType.PROFILE0)
        rep_heroes = []
        account_perks = []
        for account_perk in ["MaxHitPoints", "RegenStat", "PetStrength", "BasicAttack", "Attack", "SpecialAttack",
                             "DamageReduction", "MaxMana"]:
            account_perks.append(wex_data["stats"]["attributes"].get("account_perks").get(account_perk, 0))
        for hero_id in wex_data["stats"]["attributes"].get("rep_hero_ids", []):
            hero_data = await request.app.ctx.profiles[account_id].get_item_by_guid(hero_id)
            rep_heroes.append({
                "itemId": hero_id,
                "templateId": hero_data.get("templateId"),
                "bIsCommander": True,
                "level": hero_data.get("attributes").get("level"),
                "skillLevel": hero_data.get("attributes").get("skill_level"),
                "upgrades": hero_data.get("attributes").get("upgrades"),
                "accountInfo": {
                    "level": wex_data["stats"]["attributes"].get("level", 0),
                    "perks": account_perks
                },
                "foilLevel": hero_data.get("attributes").get("foil_lvl", -1),
                "gearTemplateId": hero_data.get("attributes").get("sidekick_template_id", ""),
            })
        results.append({
            "accountId": account_data["_id"],
            "best_gift": 0,  # These stats are unique to the friend instance on the profile, not the friend
            "lifetime_gifted": 0,  # TODO: implement gift statistics per profile
            "snapshot": {
                "displayName": account_data["displayName"],
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": rep_heroes,
                "lastPlayTime": wex_data["updated"],
                "numLevelsCompleted": wex_data["stats"]["attributes"].get("num_levels_completed", 0),
                "numTerritoriesClaimed": wex_data["stats"]["attributes"].get("num_territories_claimed", 0),
                "accountLevel": wex_data["stats"]["attributes"].get("level", 0),
                "numRepHeroes": len(wex_data["stats"]["attributes"].get("rep_hero_ids", [])),
                "isPvPUnlocked": wex_data["stats"]["attributes"].get("is_pvp_unlocked", False)
            }
        })
    if not results:
        raise errors.com.epicgames.world_explorers.not_found(errorMessage="No friends found")
    return sanic.response.json(results)
