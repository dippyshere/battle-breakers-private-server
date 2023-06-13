"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the favicon image
"""
import aiofiles
import sanic

from utils.sanic_gzip import Compress

compress = Compress()
favicon = sanic.Blueprint("favicon")


# undocumented
@favicon.route("favicon.ico", methods=["GET"])
@compress.compress()
async def favicon_image(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    Get the favicon image

    :param request: The request object
    :return: The response object
    """
    async with aiofiles.open("res/site-meta/favicon.ico", "rb") as file:
        return sanic.response.raw(await file.read(), content_type="image/x-icon")
