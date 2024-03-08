"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the ID auth exchange handling
"""
import sanic

from utils import types
from utils.exceptions import errors

from utils.sanic_gzip import Compress

compress = Compress()
id_exchange = sanic.Blueprint("id_exchange")


# stub
@id_exchange.route("/id/api/exchange", methods=["POST"])
@compress.compress()
async def id_exchange_route(request: types.BBRequest) -> sanic.response.JSONResponse:
    """
    Exchanges an auth token for another token
    :param request: The request object
    :return: The response object
    """
    # {
    #     "code": "",
    # #     "creatingClientId": "",
    # #     "expiresInSeconds": 14400,
    # }
    raise errors.com.epicgames.not_found()
