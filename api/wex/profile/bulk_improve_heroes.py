"""
Handles bulk improve heroes (used for auto upgrade)
"""

import sanic

wex_profile_bulk_improve_heroes = sanic.Blueprint("wex_profile_bulk_improve_heroes")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/BulkImproveHeroes.md
@wex_profile_bulk_improve_heroes.route("/wex/api/game/v2/profile/<accountId>/BulkImproveHeroes", methods=["POST"])
async def bulk_improve_heroes(request, accountId):
    """
    This endpoint is used to upgrade heroes in bulk
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    # TODO: Bulk improve heroes
    return sanic.response.empty(status=200)
