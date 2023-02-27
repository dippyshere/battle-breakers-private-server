"""
Handles entitlement check
"""

import sanic

wex_entitlement = sanic.Blueprint("wex_entitlement")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/entitlementCheck.md
@wex_entitlement.route("/wex/api/entitlementCheck", methods=["GET"])
async def entitlement_check(request):
    """
    This endpoint is used to check if the user has access to the game.
    :param request: The request object
    :return: The response object (204)
    """
    return sanic.response.empty()
