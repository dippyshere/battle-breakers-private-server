"""
Handles the tax calculation
"""

import sanic
import orjson

wex_catalog = sanic.Blueprint("wex_catalog")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/storefront/v2/catalog.md
@wex_catalog.route("/wex/api/storefront/v2/catalog", methods=["GET"])
async def catalog(request):
    """
    get calendar timeline
    :param request: The request object
    :return: The response object
    """
    with open("res/wex/api/storefront/v2/catalog.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
