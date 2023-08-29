"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the last online presence request
"""
import os

import sanic

from utils.friend_system import PlayerFriends
from utils.profile_system import PlayerProfile
from utils.enums import ProfileType
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
lastonline = sanic.Blueprint("presence_lastonline")


# undocumented
@lastonline.route("/api/v1/_/<accountId>/last-online", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def last_online(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Get the last online time

    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    if accountId not in request.app.ctx.friends:
        request.app.ctx.friends[accountId] = PlayerFriends(accountId)
    request.ctx.friends = request.app.ctx.friends[accountId]
    accounts_list = os.listdir("res/account/api/public/account")
    accounts_list = [account.split(".")[0] for account in accounts_list]
    response = {}
    for friend in (await request.ctx.friends.get_friends())["friends"]:
        if friend["accountId"] in accounts_list:
            if friend["accountId"] not in request.app.ctx.profiles:
                request.app.ctx.profiles[friend["accountId"]] = await PlayerProfile.init_profile(friend["accountId"])
            wex_data = await request.app.ctx.profiles[friend["accountId"]].get_profile(ProfileType.PROFILE0)
            response[friend["accountId"]] = [
                {
                    "last_online": wex_data["updated"]
                }
            ]
    return sanic.response.json(response)
