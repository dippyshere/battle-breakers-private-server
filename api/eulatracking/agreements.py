"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the eula tracking
"""

import sanic

from utils import types
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
agreements = sanic.Blueprint("eula_agreements")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/EULA%20Tracking%20Service/eulatracking/api/public/agreements/egstore/account/accountId.md
@agreements.route("/api/public/agreements/egstore/account/<accountId>", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def eula_agreements(request: types.BBRequest, accountId: str) -> sanic.response.HTTPResponse:
    """
    track eula agreements
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.empty()
