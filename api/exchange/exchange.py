"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the exchange of auth from game to web
"""
import urllib.parse

import jwt
import sanic

from utils import types
from utils.exceptions import errors
from utils.sanic_gzip import Compress
from utils.utils import public_key

compress = Compress()
exchange = sanic.Blueprint("exchange")


# undocumented
@exchange.route("/exchange", methods=["GET"])
@compress.compress()
async def exchange_route(request: types.BBRequest) -> sanic.response.HTTPResponse:
    """
    handle exchange of auth from game to web
    :param request: The request object
    :return: The response object
    """
    try:
        token = jwt.decode(request.args.get("exchangeCode"), public_key, algorithms=["RS256"], leeway=20)
        if token["jti"] in request.app.ctx.invalid_tokens:
            raise errors.com.epicgames.account.auth_token.unknown_oauth_session()
        else:
            redirect_url = urllib.parse.urlparse(request.args.get("redirectUrl"))
            redirect_url = request.args.get("redirectUrl").replace(f"{redirect_url.scheme}://", "").replace(
                redirect_url.netloc, "")
            return sanic.response.redirect(redirect_url)
    except Exception as e:
        if isinstance(e, errors.com.epicgames.account.auth_token.unknown_oauth_session):
            raise e
        else:
            raise errors.com.epicgames.common.authentication.authentication_failed()
