"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the exchange request
"""
import sanic
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
exchange = sanic.Blueprint("exchange_token")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/Account%20Service/account/api/oauth/exchange.md
@exchange.route("/api/oauth/exchange", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def exchange_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Handles the exchange token request
    :param request: The request object
    :return: The response object
    """
    if request.headers.get('Authorization'):
        token = await request.app.ctx.parse_eg1(request.headers.get("Authorization"))
        if token is not None:
            return sanic.response.json({
                "expiresInSeconds": 28800,
                "code": await request.app.ctx.generate_authorisation_eg1(token.get('sub'), token.get('dn'),
                                                                         token.get('clid')),
                "creatingClientId": token.get('clid'),
            })
        else:
            raise sanic.exceptions.Unauthorized(context={
                "errorCode": "errors.com.epicgames.common.oauth.invalid_token",
                "errorMessage": "Your exchange code has expired. Please login again"})
    else:
        raise sanic.exceptions.Unauthorized(context={
            "errorCode": "errors.com.epicgames.common.oauth.invalid_token",
            "errorMessage": "No authorisation header was found"})
