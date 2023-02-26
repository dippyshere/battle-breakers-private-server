"""
Handles the external auths endpoint
"""

import sanic

external_auths = sanic.Blueprint("account_external_auths")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e21/externalAuths.md
@external_auths.route("/account/api/public/account/<accountid>/externalAuths", methods=["GET"])
async def external_auth(request, accountid):
    """
    Get external auths
    :param request: The request object
    :param accountid: The account id
    :return: The response object
    """
    return sanic.response.json([])
