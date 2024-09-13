"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the silly 3rd party trackers
iosevent seen in 1.84
"""

import sanic

from utils import types
from utils.sanic_gzip import Compress

compress = Compress()
iosevent = sanic.Blueprint("iosevent")


# undocumented
@iosevent.route("/api/v4/iosevent", methods=["POST"])
@compress.compress()
async def ios_event(request: types.BBRequest) -> sanic.response.JSONResponse:
    """
    Responds with an empty dummy response
    :param request: The request object
    :return: The response object (200)
    """
    return sanic.response.json({})
