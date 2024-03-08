"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the enabled features stub
"""

import sanic

from utils import types
from utils.sanic_gzip import Compress

compress = Compress()
wex_enabled_features = sanic.Blueprint("wex_enabled_features")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/v2/versioncheck/Windows.md
@wex_enabled_features.route("/api/game/v2/enabled_features", methods=['GET'])
@compress.compress()
async def enabled_features(request: types.BBRequest) -> sanic.response.JSONResponse:
    """
    Handles the enabled features check.
    :param request: The request object
    :return: The response object
    """
    # Unsure what could/should be here, this feature was disabled via config files after 1.80 on pc
    return sanic.response.json([])
