"""
Handles level blitz for burny mines
"""

import sanic

wex_profile_blitz_level = sanic.Blueprint("wex_profile_blitz_level")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/BlitzLevel.md
@wex_profile_blitz_level.route("/wex/api/game/v2/profile/<accountId>/BlitzLevel", methods=["POST"])
async def blitz_level(request, accountId):
    """
    This endpoint is used to blitz a level
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    # TODO: Blitz level
    return sanic.response.empty(status=200)
