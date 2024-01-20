"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the robots.txt file
"""
import sanic

from utils.sanic_gzip import Compress

compress = Compress()
robots = sanic.Blueprint("robots")


# undocumented
@robots.route("robots.txt", methods=["GET"])
@compress.compress()
async def robots_txt(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    Get the robots.txt file

    :param request: The request object
    :return: The response object
    """
    return sanic.response.text("User-agent: *\nDisallow: /", content_type="text/plain")
