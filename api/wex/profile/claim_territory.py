"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles claiming territory
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_claim_territory = sanic.Blueprint("wex_profile_claim_territory")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/ClaimTerritory.md
@wex_profile_claim_territory.route("/<accountId>/ClaimTerritory", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def claim_territory(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to claim a territory when completing all 1/2/3/4 star missions in a zone
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    raise errors.com.epicgames.not_implemented()
