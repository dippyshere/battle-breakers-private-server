"""
Handles level abandon/exit profile mcp
"""

import sanic

wex_profile_remove_from_monster_pit = sanic.Blueprint("wex_profile_remove_from_monster_pit")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/RemoveFromMonsterPit.md
@wex_profile_remove_from_monster_pit.route("/wex/api/game/v2/profile/<accountId>/RemoveFromMonsterPit", methods=["POST"])
async def remove_from_monster_pit(request, accountId):
    """
    This endpoint is used to abandon the level
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    return sanic.response.empty(status=200)
