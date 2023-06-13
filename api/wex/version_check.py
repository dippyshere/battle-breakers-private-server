"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the version check
"""

import sanic

from utils.sanic_gzip import Compress

compress = Compress()
wex_version_check = sanic.Blueprint("wex_version_check")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/v2/versioncheck/Windows.md
@wex_version_check.route("/api/v2/versioncheck/<platform>", methods=['GET'])
@compress.compress()
async def version_check(request: sanic.request.Request, platform: str) -> sanic.response.HTTPResponse:
    """
    Handles the version check request
    :param request: The request object
    :param platform: The platform
    :return: The response object
    """
    return sanic.response.json({"type": "NO_UPDATE"})
