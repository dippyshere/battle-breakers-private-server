"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles removing a hero from all parties
"""

import sanic

from utils import types
from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_remove_hero_from_all_parties = sanic.Blueprint("wex_profile_remove_hero_from_all_parties")


# undocumented
@wex_profile_remove_hero_from_all_parties.route("/<accountId>/RemoveHeroFromAllParties", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def remove_hero_parties(request: types.BBProfileRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to remove a hero from all parties.
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    raise errors.com.epicgames.not_implemented()
