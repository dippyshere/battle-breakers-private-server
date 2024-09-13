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
helpshift = sanic.Blueprint("helpshift")


# undocumented
@helpshift.route("/api/lib/3/config", methods=["GET"])
@compress.compress()
async def helpshift_config(request: types.BBRequest) -> sanic.response.HTTPResponse:
    """
    Responds with an empty dummy response
    :param request: The request object
    :return: The response object (204)
    """
    return sanic.response.empty()
