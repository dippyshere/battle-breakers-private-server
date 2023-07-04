"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the token requests
"""
import base64

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
token = sanic.Blueprint("account_token")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/token.md
@token.route("/api/oauth/token", methods=["POST"])
@auth(allow_basic=True)
@compress.compress()
async def oauth_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Handles the oauth token request
    :param request: The request object
    :return: The response object
    """
    if request.headers.get('Authorization'):
        if request.headers.get('Authorization').startswith('basic'):
            try:
                # TODO: add supported client ids
                client_id = base64.b64decode(request.headers.get('Authorization').split(' ')[1]).decode().split(':')[0]
            except:
                raise errors.com.epicgames.common.oauth.invalid_client()
        elif request.headers.get('Authorization').startswith('bearer'):
            client_id = "3cf78cd3b00b439a8755a878b160c7ad"
        else:
            raise errors.com.epicgames.common.oauth.oauth_error()
        match request.form.get('grant_type'):
            case 'client_credentials':
                return sanic.response.json((await request.app.ctx.oauth_client_response(client_id)))
            case 'external_auth':
                if request.form.get('external_auth_type') != 'google':
                    raise errors.com.epicgames.account.ext_auth.unknown_external_auth_type()
                # TODO: Investigate external auth when there is no linked account
                # TODO: Investigate and implement proper external auth if possible
                sub = request.form.get('external_auth_token').split(':')[0]
                account = await request.app.ctx.read_file(f"res/account/api/public/account/{sub}.json")
                dn = account['displayName']
                dvid = request.headers.get('X-Epic-Device-ID')
                return sanic.response.json((await request.app.ctx.oauth_response(client_id, dn, dvid, sub)))
            case 'authorization_code':
                token = await request.app.ctx.parse_eg1(request.form.get('code'))
                if token is not None:
                    return sanic.response.json((await request.app.ctx.oauth_response(client_id, token['dn'],
                                                                                     request.headers.get('X-Epic-Device-ID'),
                                                                                     token['sub'])))
                else:
                    raise errors.com.epicgames.account.oauth.expired_authorization_code()
            case 'refresh_token':
                token = await request.app.ctx.parse_eg1(request.form.get('refresh_token'))
                if token is not None:
                    return sanic.response.json((await request.app.ctx.oauth_response(client_id, token['dn'],
                                                                                     request.headers.get('X-Epic-Device-ID'),
                                                                                     token['sub'])))
                else:
                    raise errors.com.epicgames.account.auth_token.invalid_refresh_token()
            case 'password':  # backwards compatibility for old clients
                account_id = await request.app.ctx.get_account_id_from_display_name(
                    request.form.get('username').split("@")[0].strip())
                password = await request.app.ctx.to_insecure_hash(request.form.get('password'))
                if account_id is None:
                    raise errors.com.epicgames.account.account_not_found(
                        request.form.get('username').split("@")[0].strip())
                account = await request.app.ctx.read_file(f"res/account/api/public/account/{account_id}.json")
                if account["extra"]["pwhash"] != password:
                    raise errors.com.epicgames.account.invalid_account_credentials()
                else:
                    return sanic.response.json((await request.app.ctx.oauth_response(client_id, account['displayName'],
                                                                                     request.headers.get(
                                                                                         'X-Epic-Device-ID'),
                                                                                     account_id)))
            case 'exchange_code':
                token = await request.app.ctx.parse_eg1(request.form.get('exchange_code'))
                if token is not None:
                    return sanic.response.json((await request.app.ctx.oauth_response(client_id, token['dn'],
                                                                                     request.headers.get(
                                                                                         'X-Epic-Device-ID'),
                                                                                     token['sub'])))
                else:
                    raise errors.com.epicgames.account.oauth.expired_exchange_code()
            case 'device_auth':
                if request.form.get('account_id'):
                    account = await request.app.ctx.read_file(
                        f"res/account/api/public/account/{request.form.get('account_id')}.json")
                    for device_auth in account["extra"]["deviceAuths"]:
                        if device_auth["deviceId"] == request.form.get('device_id'):
                            if device_auth["secret"] == request.form.get('secret'):
                                return sanic.response.json(
                                    (await request.app.ctx.oauth_response(client_id, account['displayName'],
                                                                          request.headers.get(
                                                                              'X-Epic-Device-ID'),
                                                                          account["id"])))
                            else:
                                raise errors.com.epicgames.common.authentication.authentication_failed(
                                    request.form.get('account_id'))
                    raise errors.com.epicgames.common.authentication.authentication_failed(
                        request.form.get('account_id'))
                else:
                    raise errors.com.epicgames.account.device_auth.invalid_device_info()
            case _:
                # TODO: misc to implement: continuation_token + device_code + otp + token_to_token
                # ALl of these except opt are unused by any client / launcher. OTP could be used in the future for 2fa.
                # otp fields: otp, challenge
                # token_to_token fields:
                # continuation_token fields:
                # device_code fields:
                raise errors.com.epicgames.common.oauth.unsupported_grant_type()
    else:
        raise errors.com.epicgames.common.oauth.invalid_request()
