"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the last online presence request
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
lastonline = sanic.Blueprint("presence_lastonline")


# undocumented
@lastonline.route("/api/v1/_/<accountId>/last-online", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def last_online(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Get the last online time

    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json({
        accountId: [{"lastOnline": "2017-09-10T00:00:00.000Z"}]
    })
