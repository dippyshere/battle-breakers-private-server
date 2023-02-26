"""
Handles the tax calculation
"""

import sanic
import orjson

price = sanic.Blueprint("priceengine_price")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/catalog-public-service-prod.ol.epicgames.com/catalog/api/shared/bulk/offers.md
@price.route("/priceengine/api/shared/offers/price", methods=["POST"])
async def price_request(request):
    """
    Get price
    :param request: The request object
    :return: The response object
    """
    with open(f"res/priceengine/api/shared/offers/price.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
