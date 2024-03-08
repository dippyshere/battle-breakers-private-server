"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the silly 3rd party trackers
app.adjust.com seen in 1.0, 1.1, 1.2
"""

import sanic

from utils import types
from utils.sanic_gzip import Compress

compress = Compress()
adjust = sanic.Blueprint("adjust")


# undocumented
@adjust.route("/session", methods=["POST"], name="adjust_session")
@adjust.route("/event", methods=["POST"], name="adjust_event")
@adjust.route("/attribution", methods=["GET"], name="attribution")
@compress.compress()
async def adjust_tracking(request: types.BBRequest) -> sanic.response.JSONResponse:
    """
    Handles the stupid tracker in older versions
    :param request: The request object
    :return: The response object (200)
    """
    return sanic.response.json({})
