"""
Handles verifying realmoney mtx mcp
"""

import sanic

wex_verify_realmoney = sanic.Blueprint("wex_verify_realmoney")


# undocumented
@wex_verify_realmoney.route("/wex/api/game/v2/profile/<accountId>/VerifyRealMoneyPurchase", methods=["POST"])
async def update_headless(request, accountId):
    """
    This endpoint is used to verify if receipts are legit or fake!!
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    return sanic.response.json({})
