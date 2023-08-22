"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the silly version info
"""

import sanic

from utils.utils import format_time

entitlement_version = sanic.Blueprint("entitlement_ver")


# undocumented
@entitlement_version.route("/api/version", methods=["GET"])
async def entitlement_version_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Version information

    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "app": "com.epicgames.entitlement.public",
        "serverDate": await format_time(),
        "overridePropertiesVersion": "unknown",
        "cln": "7f4d5cae3e9c42acf3c2c297071a482095843110",
        "build": "b2350",
        "moduleName": "PublicService",
        "buildDate": "2023-04-25T03:06:34.516Z",
        "version": "1.21.4",
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
