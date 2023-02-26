"""
Handles the namespace offers for epic catalog
"""

import sanic
import orjson

namespace = sanic.Blueprint("catalog_namespace")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/catalog-public-service-prod06.ol.epicgames.com/catalog/api/shared/namespace/wex/bulk/items.md
@namespace.route("/catalog/api/shared/bulk/namespace/wex/bulk/items", methods=["GET"])
async def items(request):
    """
    Get items
    :param request: The request object
    :return: The response object
    """
    with open(f"res/catalog/api/shared/namespace/wex/bulk/items.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
