"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the store catalog
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_receipts = sanic.Blueprint("wex_receipts")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/receipts/v1/account/ec0ebb7e56f6454e86c62299a7b32e21/receipts.md
@wex_receipts.route("/api/receipts/v1/account/<accountId>/receipts", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def receipts(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    get receipts
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json(await request.app.ctx.read_file(f"res/wex/api/receipts/v1/account/{accountId}.json"))
