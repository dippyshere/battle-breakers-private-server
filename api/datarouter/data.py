"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the telemetry data from the client
"""

import sanic

from utils.sanic_gzip import Compress

compress = Compress()
data = sanic.Blueprint("datarouter_data")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/datarouter.ol.epicgames.com/datarouter/api/v1/public/data.md
@data.route("/api/v1/public/data", methods=["POST"])
@compress.compress()
async def datarouter(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    Handles the datarouter requests (telemetry)
    :param request: The request object
    :return: The response object (204)
    """
    return sanic.response.empty()
