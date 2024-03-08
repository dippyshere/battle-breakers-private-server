"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the robots.txt file
"""
import sanic

from utils import types
from utils.sanic_gzip import Compress

compress = Compress()
robots = sanic.Blueprint("robots")


# undocumented
@robots.route("robots.txt", methods=["GET"])
@compress.compress()
async def robots_txt(request: types.BBRequest) -> sanic.response.HTTPResponse:
    """
    Get the robots.txt file

    :param request: The request object
    :return: The response object
    """
    return sanic.response.text("User-agent: *\nDisallow: /", content_type="text/plain")
