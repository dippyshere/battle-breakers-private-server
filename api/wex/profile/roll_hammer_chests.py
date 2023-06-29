"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles level abandon/exit profile mcp
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_roll_hammer_chests = sanic.Blueprint("wex_profile_roll_hammer_chests")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/RollHammerChests.md
@wex_profile_roll_hammer_chests.route("/<accountId>/RollHammerChests", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def roll_hammer_chests(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to abandon the level
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    raise errors.com.epicgames.not_found()
