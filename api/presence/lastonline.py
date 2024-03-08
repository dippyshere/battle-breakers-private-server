"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the last online presence request
"""

import sanic

from utils import types
from utils.friend_system import PlayerFriends
from utils.enums import ProfileType
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
lastonline = sanic.Blueprint("presence_lastonline")


# undocumented
@lastonline.route("/api/v1/_/<accountId>/last-online", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def last_online(request: types.BBRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get the last online time

    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    if accountId not in request.app.ctx.friends:
        request.app.ctx.friends[accountId] = await PlayerFriends.init_friends(accountId)
    response = {}
    pending_presence = []
    for friend in (await request.app.ctx.friends[accountId].get_friends())["friends"]:
        if friend["accountId"] in request.app.ctx.profiles:
            wex_data = await request.app.ctx.profiles[friend["accountId"]].get_profile(ProfileType.PROFILE0)
            response[friend["accountId"]] = [
                {
                    "last_online": wex_data["updated"]
                }
            ]
        else:
            pending_presence.append(friend)
    if len(pending_presence) > 0:
        async for wex_data in request.app.ctx.db["profile_profile0"].find({"_id": {"$in": pending_presence}}, {
            "_id": 1,
            "updated": 1
        }):
            response[wex_data["_id"]] = [
                {
                    "last_online": wex_data["updated"]
                }
            ]
    return sanic.response.json(response)
