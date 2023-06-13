"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles updating friends
"""
import datetime
import os

import sanic

from utils.friend_system import PlayerFriends
from utils.profile_system import PlayerProfile, ProfileType
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_update_friends = sanic.Blueprint("wex_profile_update_friends")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpdateFriends.md
@wex_profile_update_friends.route("/<accountId>/UpdateFriends", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def update_friends(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to update the friends list details
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    friend_instances = await request.ctx.profile.find_item_by_template_id("Friend:Instance", request.ctx.profile_id)
    accounts_list = [acc.split(".")[0] for acc in os.listdir("res/account/api/public/account/")]
    if accountId not in request.app.ctx.friends:
        request.app.ctx.friends[accountId] = PlayerFriends(accountId)
    friends_list = (await request.app.ctx.friends[accountId].get_summary())["friends"]
    result = []
    for friend in friends_list:
        if friend["accountId"] in accounts_list:
            result.append(friend["accountId"])
    for itemId in friend_instances:
        friend_instance = await request.ctx.profile.get_item_by_guid(itemId, request.ctx.profile_id)
        if friend_instance["attributes"]["accountId"] in result:
            result.remove(friend_instance["attributes"]["accountId"])
        if datetime.datetime.strptime(friend_instance["attributes"]["snapshot_expires"],
                                      "%Y-%m-%dT%H:%M:%S.%fZ") <= datetime.datetime.utcnow():
            try:
                account_data = await request.app.ctx.read_file(
                    f"res/account/api/public/account/{friend_instance['attributes']['accountId']}.json")
            except FileNotFoundError:
                await request.ctx.profile.change_item_attribute(itemId, "status", "SuggestedLegacy",
                                                                request.ctx.profile_id)
                await request.ctx.profile.change_item_attribute(itemId, "snapshot_expires",
                                                                await request.app.ctx.format_time(
                                                                    datetime.datetime.utcnow() + datetime.timedelta(
                                                                        hours=3)), request.ctx.profile_id)
                continue
            if friend_instance["attributes"]["accountId"] not in request.app.ctx.profiles:
                request.app.ctx.profiles[friend_instance["attributes"]["accountId"]] = PlayerProfile(
                    friend_instance["attributes"]["accountId"])
            wex_data = await request.app.ctx.profiles[friend_instance["attributes"]["accountId"]].get_profile(
                ProfileType.PROFILE0)
            rep_heroes = []
            account_perks = []
            for account_perk in ["MaxHitPoints", "RegenStat", "PetStrength", "BasicAttack", "Attack", "SpecialAttack",
                                 "DamageReduction", "MaxMana"]:
                account_perks.append(wex_data["stats"]["attributes"].get("account_perks").get(account_perk, 0))
            for hero_id in wex_data["stats"]["attributes"].get("rep_hero_ids", []):
                hero_data = await request.app.ctx.profiles[friend_instance["attributes"]["accountId"]].get_item_by_guid(
                    hero_id)
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
            await request.ctx.profile.change_item_attribute(itemId, "snapshot", {
                "displayName": account_data["displayName"],
                "avatarUrl": "wex-temp-avatar.png",
                "repHeroes": rep_heroes,
                "lastPlayTime": wex_data["updated"],
                "numLevelsCompleted": wex_data["stats"]["attributes"].get("num_levels_completed", 0),
                "numTerritoriesClaimed": wex_data["stats"]["attributes"].get("num_territories_claimed", 0),
                "accountLevel": wex_data["stats"]["attributes"].get("level", 0),
                "numRepHeroes": len(wex_data["stats"]["attributes"].get("rep_hero_ids", [])),
                "isPvPUnlocked": wex_data["stats"]["attributes"].get("is_pvp_unlocked", False)
            }, request.ctx.profile_id)
            await request.ctx.profile.change_item_attribute(itemId, "canBeSparred",
                                                            wex_data["stats"]["attributes"].get("is_pvp_unlocked",
                                                                                                False),
                                                            request.ctx.profile_id)
            await request.ctx.profile.change_item_attribute(itemId, "status", "Friend", request.ctx.profile_id)
            await request.ctx.profile.change_item_attribute(itemId, "snapshot_expires",
                                                            await request.app.ctx.format_time(
                                                                datetime.datetime.utcnow() + datetime.timedelta(
                                                                    hours=3)), request.ctx.profile_id)
    for friend in result:
        account_data = await request.app.ctx.read_file(
            f"res/account/api/public/account/{friend}.json")
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
