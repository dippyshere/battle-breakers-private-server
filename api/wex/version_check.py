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
    # We want to allow all clients to connect, regardless of platform or version
    # If we wanted to force a specific version / platform, we would just check the version query parameter
    # and return a SOFT_UPDATE for a content update, or a HARD_UPDATE for a client update
    # The client supports NO_UPDATE, NOT_ENABLED, SOFT_UPDATE, HARD_UPDATE, APP_REDIRECT (mobile only)
    return sanic.response.json({"type": "NO_UPDATE"})
