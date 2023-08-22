"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account sign up request for mobile
"""
import mimetypes

import aiofiles
import sanic

import urllib.parse

from utils.sanic_gzip import Compress
from utils.utils import oauth_response

compress = Compress()
register_login = sanic.Blueprint("register_login")


# undocumented
@register_login.route("/id/register", methods=["GET"], strict_slashes=False)
@compress.compress()
async def register_page(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to get the registration page
    :param request: The request object
    :return: The response object
    """
    async with aiofiles.open("res/account/login/guided/index.html", "rb") as file:
        return sanic.response.raw(await file.read(), content_type="text/html")


@register_login.route("/id/register/<file>", methods=["GET"])
@compress.compress()
async def login_page_files(request: sanic.request.Request, file: str) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to get supporting files for the site
    :param request: The request object
    :param file: The file to get
    :return: The response object
    """
    if file == "main.css":
        async with aiofiles.open("res/account/login/guided/main.css", "rb") as file:
            return sanic.response.raw(await file.read(), content_type="text/css")
    elif file == "login-script.js":
        async with aiofiles.open("res/account/login/register/signup-script.js", "rb") as file:
            return sanic.response.raw(await file.read(), content_type="text/javascript")
    else:
        if urllib.parse.unquote(file).split(".")[-1] == "woff2":
            content_type = "font/woff2"
        else:
            content_type = mimetypes.guess_type(f"res/site-meta/{urllib.parse.unquote(file)}", False)[0] or "text/plain"
        async with aiofiles.open(f"res/site-meta/{urllib.parse.unquote(file)}", "rb") as file:
            return sanic.response.raw(await file.read(), content_type=content_type)


# undocumented
@register_login.route("/id/registertest", methods=["GET"])
@compress.compress()
async def register_test(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    This endpoint is used to get the registration page
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json(
        await oauth_response("3cf78cd3b00b439a8755a878b160c7ad", "Dippyshere MbnM",
                             None,
                             "ec0ebb7e56f6454e86c62299a7b32e20"))
    # return sanic.response.text(str(request.app.ctx.profiles))
