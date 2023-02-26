"""
Handles the bulk offers for wex catalog
"""

import sanic
import orjson

bulk = sanic.Blueprint("catalog_bulk")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/catalog-public-service-prod.ol.epicgames.com/catalog/api/shared/bulk/offers.md
@bulk.route("/catalog/api/shared/bulk/offers", methods=["GET"])
async def offers(request):
    """
    Get offers
    :param request: The request object
    :return: The response object
    """
    with open(f"res/catalog/api/shared/bulk/offers.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
