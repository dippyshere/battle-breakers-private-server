"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles promoting a hero.
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_promote_hero = sanic.Blueprint("wex_profile_promote_hero")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/PromoteHero.md
@wex_profile_promote_hero.route("/<accountId>/PromoteHero", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def promote_hero(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to promote a hero.
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # errors.com.epicgames.modules.gameplayutils.recipe_failed - Unable to promote
    raise errors.com.epicgames.not_implemented()
