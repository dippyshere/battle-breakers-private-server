"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles level blitz for burny mines
"""

import sanic

from utils import types
from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_blitz_level = sanic.Blueprint("wex_profile_blitz_level")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/BlitzLevel.md
@wex_profile_blitz_level.route("/<accountId>/BlitzLevel", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def blitz_level(request: types.BBProfileRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to blitz a level
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: Blitz level
    raise errors.com.epicgames.not_implemented()
