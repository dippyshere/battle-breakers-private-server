"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the enabled features request
"""

import sanic

from utils.sanic_gzip import Compress

compress = Compress()
wex_enabled_features = sanic.Blueprint("wex_enabled_features")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/v2/versioncheck/Windows.md
@wex_enabled_features.route("/api/v2/enabled_features", methods=['GET'])
@compress.compress()
async def enabled_features(request: sanic.request.Request, platform: str) -> sanic.response.JSONResponse:
    """
    Handles the enabled features check. I HATE all those stupid clones of the same open source "private server"; none of them give correct or accurate responses ffs. i dont know what should actually be here ;/
    :param request: The request object
    :param platform: The platform
    :return: The response object
    """
    return sanic.response.json(["store", "pvp"])
