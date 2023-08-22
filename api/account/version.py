"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the silly version info
"""

import sanic

from utils.sanic_gzip import Compress
from utils.utils import format_time

compress = Compress()
account_version = sanic.Blueprint("account_ver")


# undocumented
@account_version.route("/api/version", methods=["GET"])
@compress.compress()
async def account_version_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Version information

    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "app": "com.epicgames.account.public",
        "serverDate": await format_time(),
        "overridePropertiesVersion": "unknown",
        "cln": "3f17e51",
        "build": "b2395",
        "moduleName": "Epic-Account-PublicService",
        "buildDate": "2023-05-08T16:43:58.987Z",
        "version": "UNKNOWN",
        "branch": "master",
        "modules": {
            "epic-common-core": {
                "cln": "b17bdc677bcec729d77eb8cd287bb50cbf4a5c1f",
                "build": "b1196",
                "buildDate": "2023-03-13T10:20:25.282Z",
                "version": "4.0.24.20230313101931",
                "branch": "master"
            }
        }
    })
