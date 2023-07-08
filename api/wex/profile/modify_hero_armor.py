"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles modifying hero armor.
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_modify_hero_armor = sanic.Blueprint("wex_profile_modify_hero_armor")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/ModifyHeroArmor.md
@wex_profile_modify_hero_armor.route("/<accountId>/ModifyHeroArmor", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def modify_hero_armor(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to modify hero armor.
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    raise errors.com.epicgames.not_implemented()
