"""
Handles the account token kill request
"""

import sanic

kill = sanic.Blueprint("account_kill")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/sessions/kill/eg1~token....md
@kill.route("/account/api/oauth/sessions/kill/<token>", methods=["DELETE"])
async def kill_auth(request, token):
    """
    kill a token
    :param request: The request object
    :param token: The token to kill
    :return: The response object
    """
    return sanic.response.empty()
