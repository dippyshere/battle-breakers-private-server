"""
Handles the entitlement checks for the launcher
"""

import sanic
import orjson

entitlement = sanic.Blueprint("entitlement")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/entitlement-public-service-prod08.ol.epicgames.com/entitlement/api/account/ec0ebb7e56f6454e86c62299a7b32e21/entitlements.md
@entitlement.route("/entitlement/api/account/<accountId>/entitlements", methods=["GET"])
async def entitlements(request, accountId):
    """
    Handles the entitlement check
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    with open(f"res/entitlement/api/account/{accountId}/entitlements.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
