"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account login request for mobile
"""
import mimetypes

import aiofiles
import sanic

import urllib.parse

from utils.sanic_gzip import Compress

compress = Compress()
guided_login = sanic.Blueprint("guided_login")


# undocumented
@guided_login.route("/id/login/guided", methods=["GET"], strict_slashes=False)
@compress.compress()
async def login_page(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to get the login page
    :param request: The request object
    :return: The response object
    """
    async with aiofiles.open("res/account/login/guided/index.html", "rb") as file:
        return sanic.response.raw(await file.read(), content_type="text/html")


@guided_login.route("/id/login/guided/<file>", methods=["GET"])
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
        if "register" in request.headers.get("Referer"):
            async with aiofiles.open("res/account/login/register/signup-script.js", "rb") as file:
                return sanic.response.raw(await file.read(), content_type="text/javascript")
        else:
            async with aiofiles.open("res/account/login/guided/login-script.js", "rb") as file:
                return sanic.response.raw(await file.read(), content_type="text/javascript")
    else:
        if urllib.parse.unquote(file).split(".")[-1] == "woff2":
            content_type = "font/woff2"
        else:
            content_type = mimetypes.guess_type(f"res/site-meta/{urllib.parse.unquote(file)}", False)[0] or "text/plain"
        async with aiofiles.open(f"res/site-meta/{urllib.parse.unquote(file)}", "rb") as file:
            return sanic.response.raw(await file.read(), content_type=content_type)


@guided_login.route("/id/login", methods=["GET"])
@compress.compress()
async def login_redirect1(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    Redirects to the login page
    :param request: The request object
    :return: The response object
    """
    return sanic.response.redirect("/id/login/guided/")


@guided_login.route("/id/exchange", methods=["GET"])
@compress.compress()
async def login_redirect2(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    Redirects to the login page
    :param request: The request object
    :return: The response object
    """
    return sanic.response.redirect("/id/login/guided/")
