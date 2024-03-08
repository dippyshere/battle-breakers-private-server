"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the IAP receipts
"""

import sanic

from utils import types
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_receipts = sanic.Blueprint("wex_receipts")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/receipts/v1/account/accountId/receipts.md
@wex_receipts.route("/api/receipts/v1/account/<accountId>/receipts", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def receipts(request: types.BBRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    get receipts
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json(
        (await request.app.ctx.db["receipts"].find_one({"_id": accountId})).get("receipts", [])
    )
