"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the CSRF code generation
"""
import os
import re

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
csrf = sanic.Blueprint("csrf")


# stub
@csrf.route("/id/api/csrf", methods=["POST"])
@compress.compress()
async def csrf(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Generates a CSRF code
    :param request: The request object
    :return: The response object
    """
    raise errors.com.epicgames.not_found()
    # return sanic.response.json({
    #     "token": re.sub(r"[^a-zA-Z0-9]", "", os.urandom(32).hex())
    # })
