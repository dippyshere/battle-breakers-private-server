"""
Handles level abandon/exit profile mcp
"""

import sanic

wex_profile_open_hero_chest = sanic.Blueprint("wex_profile_open_hero_chest")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/OpenHeroChest.md
@wex_profile_open_hero_chest.route("/wex/api/game/v2/profile/<accountId>/OpenHeroChest", methods=["POST"])
async def open_hero_chest(request, accountId):
    """
    This endpoint is used to abandon the level
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    return sanic.response.empty()
