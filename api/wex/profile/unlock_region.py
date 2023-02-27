"""
Handles level abandon/exit profile mcp
"""

import sanic

wex_profile_unlock_region = sanic.Blueprint("wex_profile_unlock_region")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UnlockRegion.md
@wex_profile_unlock_region.route("/wex/api/game/v2/profile/<accountId>/UnlockRegion", methods=["POST"])
async def unlock_region(request, accountId):
    """
    This endpoint is used to abandon the level
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    return sanic.response.empty()
