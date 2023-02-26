"""
Handles the token requests
"""

import sanic
import datetime
import string
import random

token = sanic.Blueprint("account_token")


def token_generator(size=32, chars=string.hexdigits):
    """
    Generates a random string of characters
    :param size: The length of the token to generate
    :param chars: The characters to use
    :return: The generated string
    """
    return ''.join(random.choice(chars).lower() for _ in range(size))


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/token.md
@token.route("/account/api/oauth/token", methods=["POST"])
async def oauth_token(request):
    """
    Handles the oauth token request
    :param request: The request object
    :return: The response object
    """
    if request.form.get('token_type') == 'eg1' and request.form.get('grant_type') == 'client_credentials':
        return sanic.response.json({
            "access_token": "eg1~eyJra0RkMyVUloRnBU.eyJhcHAiYmI3ZTU.hOmWdC7zo3u1mr62gONE7",
            "expires_in": 14400,
            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=14400)).strftime(
                "%Y-%m-%dT%H:%M:%S.000Z"),
            "token_type": "bearer",
            "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
            "internal_client": True,
            "client_service": "wex"
        })
    elif request.form.get('token_type') == 'eg1' and request.form.get('grant_type') == 'exchange_code':
        return sanic.response.json({
            "access_token": "eg1~eyJra0RkMyVUloRnBU.eyJhcHAiYmI3ZTU.hOmWdC7zo3u1mr62gONE7",
            "expires_in": 28800,
            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=28800)).strftime("%Y-%m-%dT%H:%M"
                                                                                                    ":%S.000Z"),
            "token_type": "bearer",
            "refresh_token": "eg1~eyJra0RkMyVUloRnBU.eyJhcHAiYmI3ZTU.hOmWdC7zo3u1mr62gONE7",
            "refresh_expires": 115200,
            "refresh_expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=115200)).strftime("%Y-%m"
                                                                                                             "-%dT%H"
                                                                                                             ":%M:%S"
                                                                                                             ".000Z"),
            "account_id": "ec0ebb7e56f6454e86c62299a7b32e21",
            "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
            "internal_client": True,
            "client_service": "wex",
            "displayName": "Dippyshere MbnM",
            "app": "wex",
            "in_app_id": "ec0ebb7e56f6454e86c62299a7b32e21",
            "device_id": "68009daed09498667a8039cce09983ec"
        })
    elif request.form.get('grant_type') == 'exchange_code':
        return sanic.response.json({
            "access_token": token_generator(),
            "expires_in": 28800,
            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=28800)).strftime("%Y-%m-%dT%H:%M"
                                                                                                    ":%S.000Z"),
            "token_type": "bearer",
            "refresh_token": token_generator(),
            "refresh_expires": 115200,
            "refresh_expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=115200)).strftime("%Y-%m"
                                                                                                             "-%dT%H"
                                                                                                             ":%M:%S"
                                                                                                             ".000Z"),
            "account_id": "ec0ebb7e56f6454e86c62299a7b32e21",
            "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
            "internal_client": True,
            "client_service": "wex",
            "displayName": "Dippyshere MbnM",
            "app": "wex",
            "in_app_id": "ec0ebb7e56f6454e86c62299a7b32e21",
            "device_id": "68009daed09498667a8039cce09983ec"
        })
    else:
        return sanic.response.json({
            "access_token": token_generator(),
            "expires_in": 14400,
            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=14400)).strftime(
                "%Y-%m-%dT%H:%M:%S.000Z"),
            "token_type": "bearer",
            "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
            "internal_client": True,
            "client_service": "wex"
        })
