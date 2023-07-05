"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles adding epic friend and fetching their wex specific data
"""
import datetime

import sanic

from utils.exceptions import errors
from utils.profile_system import PlayerProfile, ProfileType
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_add_epic_friend = sanic.Blueprint("wex_profile_add_epic_friend")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/AddEpicFriend.md
@wex_profile_add_epic_friend.route("/<accountId>/AddEpicFriend", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def add_epic_friend(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to fetch a new friend's wex data
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: Investigate old clients
    try:
        account_data = await request.app.ctx.read_file(
            f"res/account/api/public/account/{request.json.get('friendAccountId')}.json")
    except:
        raise errors.com.epicgames.world_explorers.not_found(
            errorMessage="Could not find friend account"
        )
    friend = request.json.get("friendAccountId")
    # TODO: resolve duplicated code
    if friend not in request.app.ctx.profiles:
        request.app.ctx.profiles[friend] = PlayerProfile(friend)
    wex_data = await request.app.ctx.profiles[friend].get_profile(ProfileType.PROFILE0)
    rep_heroes = []
    account_perks = []
    for account_perk in ["MaxHitPoints", "RegenStat", "PetStrength", "BasicAttack", "Attack", "SpecialAttack",
                         "DamageReduction", "MaxMana"]:
        account_perks.append(wex_data["stats"]["attributes"].get("account_perks").get(account_perk, 0))
    for hero_id in wex_data["stats"]["attributes"].get("rep_hero_ids", []):
        hero_data = await request.app.ctx.profiles[friend].get_item_by_guid(hero_id)
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
    await request.ctx.profile.add_item({
        "templateId": "Friend:Instance",
        "attributes": {
            "lifetime_claimed": 0,
            "accountId": account_data["id"],
            "canBeSparred": False,
            "snapshot_expires": await request.app.ctx.format_time(
                datetime.datetime.utcnow() + datetime.timedelta(hours=3)),
            "best_gift": 0,  # These stats are unique to the friend instance on the profile, not the friend
            "lifetime_gifted": 0,
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
            },
            "remoteFriendId": "",
            "status": "Friend",
            "gifts": {}
        },
        "quantity": 1
    }, profile_id=ProfileType.FRIENDS)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
