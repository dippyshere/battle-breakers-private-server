"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account token kill request
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
kill = sanic.Blueprint("account_kill")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/sessions/kill/eg1~token....md
@kill.route("/api/oauth/sessions/kill/<token>", methods=["DELETE"])
@auth
@compress.compress()
async def kill_auth(request: sanic.request.Request, token: str) -> sanic.response.HTTPResponse:
    """
    kill a token
    :param request: The request object
    :param token: The token to kill
    :return: The response object
    """
    # since tokens are stateless jwt tokens, we can't really kill them yet
    return sanic.response.empty()


# undocumented
@kill.route("/api/oauth/sessions/kill", methods=["DELETE"])
@auth
@compress.compress()
async def kill_others_account_client_service(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    kill a token but quirky this time
    :param request: The request object
    :return: The response object
    """
    return sanic.response.empty()
