"""
Handles update headless mcp
"""

import sanic

wex_update_headless = sanic.Blueprint("wex_update_headless")


# undocumented
@wex_update_headless.route("/wex/api/game/v2/profile/<accountId>/UpdateAccountHeadlessStatus", methods=["POST"])
async def update_headless(request, accountId):
    """
    This endpoint is used to do unknown magical things
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    return sanic.response.empty()
