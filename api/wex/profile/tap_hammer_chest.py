"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles tapping the hammer chest.
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_tap_hammer_chest = sanic.Blueprint("wex_profile_tap_hammer_chest")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/TapHammerChest.md
@wex_profile_tap_hammer_chest.route("/<accountId>/TapHammerChest", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def tap_hammer_chest(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to tap the hammer chest
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    raise sanic.exceptions.SanicException("Not implemented", 501, quiet=True)
