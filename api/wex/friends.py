"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the manifest
"""
import urllib.parse

import sanic

from utils.profile_system import PlayerProfile, ProfileType
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
    account_id = request.match_info.get('accountId')
    if account_id is not None:
        if account_id not in request.app.ctx.profiles:
            request.app.ctx.profiles[account_id] = PlayerProfile(account_id)
        request.ctx.profile = request.app.ctx.profiles[account_id]
    else:
        request.ctx.profile = None
    if request.args.get("rvn") is None:
        request.ctx.rvn = -1
    else:
        try:
            request.ctx.rvn = int(request.args.get("rvn"))
        except:
            request.ctx.rvn = -1
    request.ctx.profile_id = ProfileType.from_string("friends")
    request.ctx.profile_revisions = request.headers.get("X-EpicGames-ProfileRevisions")
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
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
