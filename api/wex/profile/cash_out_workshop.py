"""
Handles workshop cash out
"""

import sanic

wex_profile_cash_out_workshop = sanic.Blueprint("wex_profile_cash_out_workshop")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/CashOutWorkshop.md
@wex_profile_cash_out_workshop.route("/wex/api/game/v2/profile/<accountId>/CashOutWorkshop", methods=["POST"])
async def cash_out_workshop(request, accountId):
    """
    This endpoint is used to exchange workshop stars to gold
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    # TODO: Cash out workshop
    return sanic.response.empty(status=200)
