"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the manifest
"""
import urllib.parse

import sanic

from utils.exceptions import errors
from utils.profile_system import PlayerProfile
from utils.enums import ProfileType
from utils.sanic_gzip import Compress
from utils.utils import search_for_display_name, read_file

compress = Compress()
wex_friend = sanic.Blueprint("wex_friend")


# undocumented
@wex_friend.route("/api/game/v2/friends/<accountId>/search", methods=['GET'])
@compress.compress()
async def wex_friends_search(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to search for friends
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    account_ids = []
    results = []
    display_name = urllib.parse.unquote(request.args.get("name", ""))
    # requested_id = await get_account_id_from_display_name(display_name)
    # if requested_id is not None:
    #     account_ids.append(requested_id)
    search_results = await search_for_display_name(display_name)
    # if requested_id is not None and requested_id in search_results:
    #     search_results.remove(requested_id)
    if search_results:
        account_ids.extend(search_results)
    for account_id in account_ids:
        account_data = await read_file(f"res/account/api/public/account/{account_id}.json")
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
            "accountId": account_data["id"],
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
