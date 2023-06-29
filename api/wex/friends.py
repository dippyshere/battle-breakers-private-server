"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the manifest
"""
import aiofiles
import sanic

from utils.exceptions import errors
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
    # TODO: Implement this
    raise errors.com.epicgames.service_unavailable()
