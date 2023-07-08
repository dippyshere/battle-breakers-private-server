"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles bulk improve heroes (used for auto upgrade)
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_bulk_improve_heroes = sanic.Blueprint("wex_profile_bulk_improve_heroes")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/BulkImproveHeroes.md
@wex_profile_bulk_improve_heroes.route("/<accountId>/BulkImproveHeroes", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def bulk_improve_heroes(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to upgrade heroes in bulk
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: Bulk improve heroes
    raise errors.com.epicgames.not_implemented()
