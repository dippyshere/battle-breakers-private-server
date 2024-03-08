"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the silly version info
"""

import sanic

from utils import types
from utils.sanic_gzip import Compress
from utils.utils import format_time

compress = Compress()
presence_version = sanic.Blueprint("presence_ver")


# undocumented
@presence_version.route("/api/version", methods=["GET"])
@compress.compress()
async def presence_version_route(request: types.BBRequest) -> sanic.response.JSONResponse:
    """
    Version information

    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "app": "presence",
        "serverDate": await format_time(),
        "overridePropertiesVersion": "unknown",
        "cln": "871585423",
        "build": "b1245",
        "moduleName": "presence-main",
        "buildDate": "2023-05-08T10:34:46.760Z",
        "version": "1.0.47",
        "branch": "trunk",
        "modules": {
            "epic-xmpp-api-v1-base": {
                "cln": "5131a23c1470acbd9c94fae695ef7d899c1a41d6",
                "build": "b3595",
                "buildDate": "2019-07-30T09:11:06.587Z",
                "version": "0.0.1",
                "branch": "master"
            },
            "epic-common-core": {
                "cln": "b17bdc677bcec729d77eb8cd287bb50cbf4a5c1f",
                "build": "b1196",
                "buildDate": "2023-03-13T10:20:25.282Z",
                "version": "4.0.24.20230313101931",
                "branch": "master"
            }
        }
    })
