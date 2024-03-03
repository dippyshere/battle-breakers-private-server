"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the silly version info
"""

import sanic

from utils.sanic_gzip import Compress
from utils.utils import format_time

compress = Compress()
eulatracking_version = sanic.Blueprint("eulatracking_ver")


# undocumented
@eulatracking_version.route("/api/version", methods=["GET"])
@compress.compress()
async def eula_version_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Version information

    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "app": "com.epicgames.eulatracking.public",
        "serverDate": await format_time(),
        "overridePropertiesVersion": "unknown",
        "cln": "5199f29252ead0c49871729f6049c4b8dcc0418c",
        "build": "b2039",
        "moduleName": "Epic-EULATracking-PublicService",
        "buildDate": "2023-04-25T03:06:34.516Z",
        "version": "1.5.42",
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
