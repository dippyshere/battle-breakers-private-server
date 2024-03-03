"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles verifying real money mtx mcp
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_verify_realmoney = sanic.Blueprint("wex_verify_realmoney")


# undocumented
@wex_verify_realmoney.route("/<accountId>/VerifyRealMoneyPurchase", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def verify_rmt(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to verify if receipts are legit or fake!! Checks for profile changes after a purchase.
    :param request: The request object
    :param accountId: The account id
    :return: The response object containing the profile changes
    """
    return sanic.response.json(
        await request.ctx.profile.construct_response(client_command_revision=request.ctx.profile_revisions)
    )
