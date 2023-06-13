"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the friend settings
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
settings = sanic.Blueprint("friends_settings")


# undocumented
@settings.route("/api/v1/<accountId>/settings", methods=["GET", "PATCH", "PUT"])
@auth(strict=True)
@compress.compress()
async def friends_settings(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Get handle friend privacy settings
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    friends = await request.ctx.friends.get_friends()
    if request.method == "GET":
        return sanic.response.json(friends["settings"])
    if request.json.get("acceptInvites") is not None:
        friends["settings"]["acceptInvites"] = request.json.get("acceptInvites")
    if request.json.get("mutualPrivacy") is not None:
        friends["settings"]["mutualPrivacy"] = request.json.get("mutualPrivacy")
    await request.ctx.friends.update_friends(friends)
    return sanic.response.json(friends["settings"])


# undocumented
@settings.route("/api/public/settings/<accountId>", methods=["GET", "PATCH", "PUT"])
@auth(strict=True)
@compress.compress()
async def friends_settings(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Get handle friend privacy settings
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    friends = await request.ctx.friends.get_friends()
    if request.method == "GET":
        return sanic.response.json(friends["settings"])
    if request.json.get("acceptInvites") is not None:
        friends["settings"]["acceptInvites"] = request.json.get("acceptInvites")
    await request.ctx.friends.update_friends(friends)
    return sanic.response.json(friends["settings"])


"""
for old client, investigate /api/public/friends/0b0f09b400854b9b98932dd9e5abe7c5?includePending=true
{
    "accountId": "09b8744abd524d879630f7c79365e2f8",
    "status": "ACCEPTED",
    "direction": "INBOUND",
    "created": "2018-09-05T14:55:04.261Z",
    "favorite": false
}
/api/public/blocklist/0b0f09b400854b9b98932dd9e5abe7c5
{"blockedUsers":["4ab7f6139b35468080f8a7b8bb4334d5"]}
"""
