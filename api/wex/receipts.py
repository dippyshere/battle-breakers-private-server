"""
Handles the store catalog
"""

import sanic
import orjson

wex_receipts = sanic.Blueprint("wex_receipts")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/receipts/v1/account/ec0ebb7e56f6454e86c62299a7b32e21/receipts.md
@wex_receipts.route("/wex/api/receipts/v1/account/<accountId>/receipts", methods=["GET"])
async def receipts(request, accountId):
    """
    get receipts
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    with open(f"res/wex/api/receipts/v1/account/{accountId}/receipts.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
