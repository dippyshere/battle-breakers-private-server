"""
Handles the eula tracking
"""

import sanic

agreements = sanic.Blueprint("eula_agreements")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/eulatracking-public-service-prod06.ol.epicgames.com/eulatracking/api/public/agreements/egstore/account/ec0ebb7e56f6454e86c62299a7b32e21.md
@agreements.route("/eulatracking/api/public/agreements/egstore/account/<accountId>", methods=["GET"])
async def friends_summary(request, accountId):
    """
    track eula agreements
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.empty()
