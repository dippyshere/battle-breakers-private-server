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
from utils.profile_system import PlayerProfile
from utils.enums import ProfileType, FriendStatus
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
    pending_changes = request.ctx.profile.friends_changes
    if accountId not in request.app.ctx.friends:
        request.app.ctx.friends[accountId] = PlayerFriends(accountId)
    friends_list = (await request.app.ctx.friends[accountId].get_summary())["friends"]
    incoming_list = (await request.app.ctx.friends[accountId].get_summary())["incoming"]
    outgoing_list = (await request.app.ctx.friends[accountId].get_summary())["outgoing"]
    result = {}
    for friend in friends_list:
        if friend["accountId"] in accounts_list:
            result[friend["accountId"]] = FriendStatus.FRIEND
    for friend in incoming_list:
        if friend["accountId"] in accounts_list:
            result[friend["accountId"]] = FriendStatus.INVITED
    for friend in outgoing_list:
        if friend["accountId"] in accounts_list:
            result[friend["accountId"]] = FriendStatus.REQUESTED
    for pending_change in pending_changes:
        # noinspection IncorrectFormatting
        if pending_change.get("changeType") == "itemAdded" and pending_change.get("item", {}).get(
                "templateId") == "Friend:Instance" and pending_change.get("item", {}).get("attributes", {}).get(
                "accountId") in accounts_list:
            result.pop(pending_change.get("item", {}).get("attributes", {}).get("accountId"))
    for itemId in friend_instances:
        friend_instance = await request.ctx.profile.get_item_by_guid(itemId, request.ctx.profile_id)
        if friend_instance["attributes"]["accountId"] in result:
            result.pop(friend_instance["attributes"]["accountId"])
        if datetime.datetime.strptime(friend_instance["attributes"]["snapshot_expires"],
                                      "%Y-%m-%dT%H:%M:%S.%fZ") <= datetime.datetime.utcnow():
            try:
                account_data = await request.app.ctx.read_file(
                    f"res/account/api/public/account/{friend_instance['attributes']['accountId']}.json")
            except FileNotFoundError:
                # This friend isn't on the private server / was deleted
                # In this case, we preserve their snapshot and entry by marking them as a legacy friend
                # SuggestedLegacy was originally intended for friends on the old (1.0-1.71) friends system,
                # suggesting players to add them back using the Epic friends system
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
        await request.ctx.profile.add_friend_instance(request, friend, result[friend])
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
