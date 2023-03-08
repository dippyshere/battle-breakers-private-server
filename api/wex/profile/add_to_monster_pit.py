"""
Handles adding heroes to monster pit
"""

import sanic

wex_profile_add_to_monster_pit = sanic.Blueprint("wex_profile_add_to_monster_pit")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/AddToMonsterPit.md
@wex_profile_add_to_monster_pit.route("/wex/api/game/v2/profile/<accountId>/AddToMonsterPit", methods=["POST"])
async def add_to_monster_pit(request, accountId):
    """
    This endpoint is used to add heroes to the monster pit
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    # TODO: Add to Monster Pit
    return sanic.response.empty(status=200)
