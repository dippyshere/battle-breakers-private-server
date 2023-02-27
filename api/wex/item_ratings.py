"""
Handles all the item ratings requests
"""

import sanic

wex_item_ratings = sanic.Blueprint("wex_item_ratings")


# https://github.com/dippyshere/battle-breakers-documentation/tree/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/item_ratings/ec0ebb7e56f6454e86c62299a7b32e21
@wex_item_ratings.route("/wex/api/game/v2/item_ratings/<accountId>/<templateId>", methods=["GET"])
async def item_ratings(request, accountId, templateId):
    """
    This endpoint is used to get item ratings from the server
    :param request: The request object
    :param accountId: The account id
    :param templateId: The template id
    :return: The response object (204)
    """
    return sanic.response.empty()
