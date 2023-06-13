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
pe_version = sanic.Blueprint("pe_ver")


# undocumented
@pe_version.route("/api/version", methods=["GET"])
@compress.compress()
async def priceengine_version_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Version information

    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "app": "com.epicgames.priceengine.public",
        "serverDate": await request.app.ctx.format_time(),
        "overridePropertiesVersion": "unknown",
        "cln": "f145af92d4871c35b8419983349f47d1c7c071bb",
        "build": "b4735",
        "moduleName": "Epic-PriceEngine-PublicService",
        "buildDate": "2023-05-11T03:17:23.565Z",
        "version": "2.49",
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
