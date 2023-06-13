"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles entitlement check
"""

import sanic

from utils.utils import authorized as auth

wex_entitlement = sanic.Blueprint("wex_entitlement")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/entitlementCheck.md
@wex_entitlement.route("/api/entitlementCheck", methods=["GET"])
@auth
async def entitlement_check(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to check if the user has access to the game, and if not, grant them (probably).
    :param request: The request object
    :return: The response object (204)
    """
    return sanic.response.empty()
