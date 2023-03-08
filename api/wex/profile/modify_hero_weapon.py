"""
Handles level abandon/exit profile mcp
"""

import sanic

wex_profile_modify_hero_weapon = sanic.Blueprint("wex_profile_modify_hero_weapon")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ModifyHeroWeapon.md
@wex_profile_modify_hero_weapon.route("/wex/api/game/v2/profile/<accountId>/ModifyHeroWeapon", methods=["POST"])
async def modify_hero_weapon(request, accountId):
    """
    This endpoint is used to abandon the level
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    return sanic.response.empty(status=200)
