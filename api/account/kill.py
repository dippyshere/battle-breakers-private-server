"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account token kill request
"""

import sanic

from utils.exceptions import errors
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
    # TODO: support killAllWithSameSource query param
    token = await request.app.ctx.parse_eg1(token)
    if token is not None:
        request.app.ctx.invalid_tokens.append(token["jti"])
    return sanic.response.empty()


# undocumented
@kill.route("/api/oauth/sessions/kill", methods=["DELETE"])
@auth
@compress.compress()
async def kill_others(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    kill a token but quirky this time
    :param request: The request object
    :return: The response object
    """
    match request.args.get("killType"):
        case "OTHERS_ACCOUNT_CLIENT_SERVICE":
            # TODO: kill all other tokens (client + account + service)
            # request.app.ctx.invalid_tokens.append(
            #    (await request.app.ctx.parse_eg1(request.headers.get("Authorization", "")))["jti"])
            return sanic.response.empty()
        case "OTHERS_ACCOUNT_CLIENT":
            # TODO: kill all other tokens (client for the account)
            return sanic.response.empty()
        case "OTHERS_SAME_SOURCE_ID":
            # TODO: kill all other tokens with the same source id
            return sanic.response.empty()
        case "OTHERS":
            # TODO: kill all other tokens (client + account)
            return sanic.response.empty()
        case "ALL":
            # TODO: kill all tokens (client + account)
            request.app.ctx.invalid_tokens.append(
                (await request.app.ctx.parse_eg1(request.headers.get("Authorization", "")))["jti"])
            return sanic.response.empty()
        case "ALL_ACCOUNT_CLIENT":
            # TODO: kill all tokens (client + account for the client)
            request.app.ctx.invalid_tokens.append(
                (await request.app.ctx.parse_eg1(request.headers.get("Authorization", "")))["jti"])
            return sanic.response.empty()
        case _:
            raise errors.com.epicgames.bad_request()
