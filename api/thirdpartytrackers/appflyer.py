"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the silly 3rd party trackers
appflyer seen in 1.71
"""

import sanic

from utils.sanic_gzip import Compress

compress = Compress()
appflyer = sanic.Blueprint("appflyer")


# undocumented
@appflyer.route("/api/v4/androidevent", methods=["POST"])
@compress.compress()
async def appflyer_event(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Handles the stupid tracker in older versions
    :param request: The request object
    :return: The response object (200)
    """
    return sanic.response.json({})
