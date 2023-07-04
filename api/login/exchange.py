"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the ID auth exchange handling
"""
import os
import re

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
id_exchange = sanic.Blueprint("id_exchange")


# stub
@id_exchange.route("/id/api/exchange", methods=["POST"])
@compress.compress()
async def id_exchange_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Exchanges an auth token for another token
    :param request: The request object
    :return: The response object
    """
    raise errors.com.epicgames.not_found()
