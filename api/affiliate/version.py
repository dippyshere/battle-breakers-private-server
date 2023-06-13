"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the silly version info
"""

import sanic

from utils.sanic_gzip import Compress

compress = Compress()
affiliate_version = sanic.Blueprint("affiliate_ver")


# undocumented
@affiliate_version.route("/api/version", methods=["GET"])
@compress.compress()
async def affiliate_version_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Version information

    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "app": "com.epicgames.affiliate.public",
        "serverDate": await request.app.ctx.format_time(),
        "overridePropertiesVersion": "unknown",
        "cln": "ae16ea55f35941e131f313f8086336a3aa4f318e",
        "build": "b2592",
        "moduleName": "Epic-Affiliate-PublicService",
        "buildDate": "2023-05-10T19:17:34.361Z",
        "version": "1.6.45",
        "branch": "TRUNK",
        "modules": {
            "epic-common-core": {
                "cln": "01b0a30780e8d1b4b4327fda403299fd635c6559",
                "build": "b1096",
                "buildDate": "2022-09-21T13:55:01.514Z",
                "version": "3.2.35.20220921145409",
                "branch": "master"
            }
        }
    })
