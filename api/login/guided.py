"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account login request for mobile
"""
import email.utils
import mimetypes

import aiofiles
import aiofiles.os
import sanic

import urllib.parse

from utils.sanic_gzip import Compress

compress = Compress()
guided_login = sanic.Blueprint("guided_login")


# undocumented
@guided_login.route("/id/login/guided", methods=["GET"], strict_slashes=False, name="login-guided")
@guided_login.route("/id/register", methods=["GET"], strict_slashes=False, name="register")
@compress.compress()
async def login_page(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to get the login page
    :param request: The request object
    :return: The response object
    """
    if request.route.name == "dippy_breakers.guided_login.register":
        last_modified = (await aiofiles.os.stat("res/account/login/guided/index.html")).st_mtime
        response = await sanic.response.validate_file(request.headers, last_modified)
        if response is not None:
            return response
        headers = {"Last-Modified": email.utils.formatdate(last_modified, usegmt=True),
                   "expires": email.utils.formatdate(last_modified + 604800, usegmt=True),
                   "cache-control": "public, max-age=604800"}
        async with aiofiles.open("res/account/login/guided/index.html", "rb") as file:
            page = (await file.read()).decode()
        page = page.replace('<script src="/id/login/guided/login-script.min.js"></script>',
                            '<script src="/id/login/guided/signup-script.min.js"></script>', 1)
        return sanic.response.HTTPResponse(page, headers=headers, content_type="text/html")
    else:
        return await sanic.response.file("res/account/login/guided/index.html", max_age=604800,
                                         request_headers=request.headers)


@guided_login.route("/id/login/guided/<file>", methods=["GET"], name="login-guided-files")
@guided_login.route("/id/register/<file>", methods=["GET"], name="register-files")
@compress.compress()
async def login_page_files(request: sanic.request.Request, file: str) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to get supporting files for the site
    :param request: The request object
    :param file: The file to get
    :return: The response object
    """
    match file:
        case "main.css" | "main.min.css":
            return await sanic.response.file("res/account/login/guided/main.min.css", max_age=604800,
                                             request_headers=request.headers)
        case "signup-script.js" | "signup-script.min.js":
            last_modified = (await aiofiles.os.stat("res/account/login/guided/login-script.js")).st_mtime
            response = await sanic.response.validate_file(request.headers, last_modified)
            if response is not None:
                return response
            headers = {"Last-Modified": email.utils.formatdate(last_modified, usegmt=True),
                       "expires": email.utils.formatdate(last_modified + 604800, usegmt=True),
                       "cache-control": "public, max-age=604800"}
            async with aiofiles.open("res/account/login/guided/login-script.min.js", "rb") as file:
                script = (await file.read()).decode()
            script = script.replace('loginFormDiv.style.display="block"',
                                    'loginFormDiv.style.display="none"', 1)
            script = script.replace('signupFormDiv.style.display="none"',
                                    'signupFormDiv.style.display="block"', 1)
            return sanic.response.HTTPResponse(script, headers=headers, content_type="application/javascript")
        case "login-script.js" | "login-script.min.js":
            return await sanic.response.file("res/account/login/guided/login-script.min.js", max_age=604800,
                                             request_headers=request.headers)
        case "webp-detection.js" | "webp-detection.min.js":
            return await sanic.response.file("res/account/login/guided/webp-detection.min.js", max_age=604800,
                                             request_headers=request.headers)
        case "index.html":
            if request.route.name == "dippy_breakers.guided_login.register-files":
                return sanic.response.redirect("/id/register")
            else:
                return sanic.response.redirect("/id/login/guided")
        case _:
            if urllib.parse.unquote(file).split(".")[-1] == "woff2":
                content_type = "font/woff2"
            else:
                content_type = mimetypes.guess_type(f"res/site-meta/{urllib.parse.unquote(file)}", False)[0] or "text/plain"
            if request.headers.get("save-data") == "on" and urllib.parse.unquote(file) in ["bb-extended-blur-hd.jpg",
                                                                                           "bb-extended-blur-hd.webp"]:
                return sanic.response.redirect(
                    f"/id/login/guided/bb-extended-blur.{urllib.parse.unquote(file).split('.')[-1]}")
            return await sanic.response.file(f"res/site-meta/{urllib.parse.unquote(file)}", max_age=604800,
                                             request_headers=request.headers, mime_type=content_type)


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


@guided_login.route("/apple-touch-icon.png", methods=["GET"], name="apple-touch-icon")
@guided_login.route("/apple-touch-icon-precomposed.png", methods=["GET"], name="apple-touch-icon-precomposed")
@compress.compress()
async def apple_touch_icon(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to get the apple touch icon
    :param request: The request object
    :return: The response object
    """
    return await sanic.response.file("res/site-meta/apple-touch-icon.png", max_age=604800,
                                     request_headers=request.headers)
