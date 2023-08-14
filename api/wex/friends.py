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
    raise errors.com.epicgames.not_implemented()
    # return sanic.response.json({
    #     "accounts": [{
    #     "accountId": "09b8744abd524d879630f7c79365e2f8",
    #     "username": "Dippyshere",
    # }],
    #     "count": 1
    # })
    # account_id = request.match_info.get('accountId')
    # if account_id is not None:
    #     if account_id not in request.app.ctx.profiles:
    #         request.app.ctx.profiles[account_id] = PlayerProfile(account_id)
    #     request.ctx.profile = request.app.ctx.profiles[account_id]
    # else:
    #     request.ctx.profile = None
    # if request.args.get("rvn") is None:
    #     request.ctx.rvn = -1
    # else:
    #     try:
    #         request.ctx.rvn = int(request.args.get("rvn"))
    #     except:
    #         request.ctx.rvn = -1
    # request.ctx.profile_id = ProfileType.from_string("friends")
    # request.ctx.profile_revisions = request.headers.get("X-EpicGames-ProfileRevisions")
    # await request.ctx.profile.add_item({
    #     "templateId": "Friend:Instance",
    #     "attributes": {
    #         "lifetime_claimed": 0,
    #         "accountId": "1e841dc603b74eb18ef12803c2b58588",
    #         "canBeSparred": False,
    #         "snapshot_expires": "2022-12-29T02:14:51.022Z",
    #         "best_gift": 0,
    #         "lifetime_gifted": 0,
    #         "remoteFriendId": "776590ce-df4b-4a31-b404-bd4fbf7e2599",
    #         "snapshot": {
    #             "displayName": "Purplereign780",
    #             "avatarUrl": "wex-temp-avatar.png",
    #             "repHeroes": [
    #                 {
    #                     "itemId": "d28e2049-5a10-4d5c-8776-c1b755480a98",
    #                     "templateId": "Character:Mage_SR2_Water_Blizzard_T06",
    #                     "bIsCommander": True,
    #                     "level": 150,
    #                     "skillLevel": 20,
    #                     "upgrades": [
    #                         95,
    #                         95,
    #                         95,
    #                         95,
    #                         34,
    #                         125,
    #                         5,
    #                         125,
    #                         5
    #                     ],
    #                     "accountInfo": {
    #                         "level": 809,
    #                         "perks": [
    #                             12,
    #                             182,
    #                             639,
    #                             185,
    #                             13,
    #                             30,
    #                             30,
    #                             30
    #                         ]
    #                     },
    #                     "foilLevel": -1,
    #                     "gearTemplateId": ""
    #                 },
    #                 {
    #                     "itemId": "27ae29f8-110e-4ad0-84ab-cf69384e4787",
    #                     "templateId": "Character:Cleric_SR1_Water_RevitalizingWaters_T06",
    #                     "bIsCommander": True,
    #                     "level": 150,
    #                     "skillLevel": 20,
    #                     "upgrades": [
    #                         95,
    #                         95,
    #                         95,
    #                         95,
    #                         34,
    #                         134,
    #                         5,
    #                         125,
    #                         5
    #                     ],
    #                     "accountInfo": {
    #                         "level": 809,
    #                         "perks": [
    #                             12,
    #                             182,
    #                             639,
    #                             185,
    #                             13,
    #                             30,
    #                             30,
    #                             30
    #                         ]
    #                     },
    #                     "foilLevel": -1,
    #                     "gearTemplateId": "Character:TreasureHunter_Starter_Water_HiddenRiver_T05"
    #                 }
    #             ],
    #             "lastPlayTime": "2020-12-21T11:58:46.424Z",
    #             "numLevelsCompleted": 1068,
    #             "numTerritoriesClaimed": 84,
    #             "accountLevel": 809,
    #             "numRepHeroes": 2,
    #             "isPvPUnlocked": True
    #         },
    #         "status": "None",
    #         "gifts": {}
    #     },
    #     "quantity": 1
    # }, profile_id=request.ctx.profile_id)
    # return sanic.response.json(
    #     await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
    #                                                  request.ctx.profile_revisions)
    # )
    # displayName = urllib.parse.unquote(request.args.get("name"))
    # requested_id = await request.app.ctx.get_account_id_from_display_name(displayName)
    # if requested_id is None:
    #     raise errors.com.epicgames.account.account_not_found(displayName)
    # account_info = await request.app.ctx.read_file(f"res/account/api/public/account/{requested_id}.json")
    # if requested_id == accountId:
    #     return sanic.response.json({
    #         "id": account_info["id"],
    #         "displayName": account_info["displayName"],
    #         "minorVerified": account_info["minorVerified"],
    #         "minorStatus": account_info["minorStatus"],
    #         "cabinedMode": account_info["cabinedMode"],
    #         "name": account_info["name"],
    #         "email": account_info["email"],
    #         "failedLoginAttempts": account_info["failedLoginAttempts"],
    #         "lastLogin": account_info["lastLogin"],
    #         "numberOfDisplayNameChanges": account_info["numberOfDisplayNameChanges"],
    #         "dateOfBirth": account_info["dateOfBirth"],
    #         "ageGroup": account_info["ageGroup"],
    #         "headless": account_info["headless"],
    #         "country": account_info["country"],
    #         "lastName": account_info["lastName"],
    #         "phoneNumber": account_info["phoneNumber"],
    #         "preferredLanguage": account_info["preferredLanguage"],
    #         "lastDisplayNameChange": account_info["lastDisplayNameChange"],
    #         "canUpdateDisplayName": account_info["canUpdateDisplayName"],
    #         "tfaEnabled": account_info["tfaEnabled"],
    #         "emailVerified": account_info["emailVerified"],
    #         "minorExpected": account_info["minorExpected"],
    #         "hasHashedEmail": account_info["hasHashedEmail"],
    #         "externalAuths": account_info["externalAuths"]
    #     })
    # return sanic.response.json({
    #     "id": account_info["id"],
    #     "displayName": account_info["displayName"],
    #     "minorVerified": account_info["minorVerified"],
    #     "minorStatus": account_info["minorStatus"],
    #     "cabinedMode": account_info["cabinedMode"],
    #     "externalAuths": account_info["externalAuths"]
    # })
