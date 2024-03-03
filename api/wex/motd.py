"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the motd of old versions
"""

import sanic

from utils.exceptions import errors
from utils.sanic_gzip import Compress

compress = Compress()
wex_motd = sanic.Blueprint("wex_motd")


# undocumented
@wex_motd.route("/api/game/v2/motd", methods=['GET'])
@compress.compress()
async def motd(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    Handles the motd of old versions
    :param request: The request object
    :return: The response object
    """
    raise errors.com.epicgames.not_implemented()
