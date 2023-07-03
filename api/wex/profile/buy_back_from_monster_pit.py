"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles monster pit buy back
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_buy_back_from_monster_pit = sanic.Blueprint("wex_profile_buy_back_from_monster_pit")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/BuyBackFromMonsterPit.md
@wex_profile_buy_back_from_monster_pit.route("/<accountId>/BuyBackFromMonsterPit", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def buy_back_from_monster_pit(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to buy back heroes and pets from the monster pit
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: Buy back from monster pit
    raise errors.com.epicgames.not_implemented()
