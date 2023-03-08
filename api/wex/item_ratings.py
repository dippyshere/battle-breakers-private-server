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
    return sanic.response.json({
        "myRating": {
            "gameplayRating": 0,
            "appearanceRating": 0
        },
        "overallRatings": {
            "ratingsKey": f"CD.{templateId.split('Character%3A')[1].replace('_', '.').replace('T06', 'T03').replace('T05', 'T03').replace('T04', 'T03')}",
            "discussUrl": "https://discord.gg/stw-dailies-757765475823517851",
            "ratings": [
                {
                    "gameplayRating": 7,
                    "appearanceRating": 4
                },
                {
                    "gameplayRating": 5,
                    "appearanceRating": 4
                },
                {
                    "gameplayRating": 20,
                    "appearanceRating": 10
                },
                {
                    "gameplayRating": 16,
                    "appearanceRating": 19
                },
                {
                    "gameplayRating": 52,
                    "appearanceRating": 63
                }
            ]
        }
    })


# undocumented
@wex_item_ratings.route("/wex/api/game/v2/item_ratings/<accountId>/<templateId>", methods=["POST"])
async def set_item_rating(request, accountId, templateId):
    """
    This endpoint is used to rate an item
    :param request: The request object
    :param accountId: The account id
    :param templateId: The template id
    :return: The response object (204)
    """
    with open(f"res/wex/api/game/v2/item_ratings/{accountId}/{templateId}.json", "wb") as file:
        file.write(request.body)
    return sanic.response.json({})
