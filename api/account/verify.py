"""
verify if a token is valid
"""

import sanic
import datetime

verify = sanic.Blueprint("account_verify")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/oauth/verify.md
@verify.route("/account/api/oauth/verify", methods=["GET"])
async def verify_auth(request):
    """
    verify game auth
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "token": f"{request.token}",
        "session_id": "9bcccd0920424ce9b110b2e50bf05ce6",
        "token_type": "bearer",
        "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
        "internal_client": True,
        "client_service": "wex",
        "account_id": "ec0ebb7e56f6454e86c62299a7b32e21",
        "expires_in": 28738,
        "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=28738)).strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"),
        "auth_method": "exchange_code",
        "display_name": "Dippyshere MbnM",
        "ext_auth_id": "1123",
        "ext_auth_type": "exchange_code",
        "ext_auth_method": "google_id_token",
        "ext_auth_display_name": "A",
        "app": "wex",
        "in_app_id": "ec0ebb7e56f6454e86c62299a7b32e21",
        "device_id": "68009daed09498667a8039cce09983ec",
        "perms": [{
            "resource": "blockList:ec0ebb7e56f6454e86c62299a7b32e21",
            "action": 14
        }, {
            "resource": "wexp:cloudstorage:system",
            "action": 2
        }, {
            "resource": "account:public:account:*",
            "action": 2
        }, {
            "resource": "account:oauth:exchangeTokenCode",
            "action": 15
        }, {
            "resource": "account:public:account",
            "action": 2
        }, {
            "resource": "priceengine:shared:offer:price",
            "action": 2
        }, {
            "resource": "xmpp:session:*:ec0ebb7e56f6454e86c62299a7b32e21",
            "action": 1
        }, {
            "resource": "wexp:wexp_role:client",
            "action": 15
        }, {
            "resource": "wexp:profile:ec0ebb7e56f6454e86c62299a7b32e21:*",
            "action": 15
        }, {
            "resource": "account:public:account:externalAuths",
            "action": 15
        }, {
            "resource": "wexp:calendar",
            "action": 2
        }, {
            "resource": "account:token:otherSessionsForAccountClient",
            "action": 8
        }, {
            "resource": "account:token:otherSessionsForAccountClientService",
            "action": 8
        }, {
            "resource": "account:public:account:deviceAuths",
            "action": 11
        }, {
            "resource": "wexp:cloudstorage:system:*",
            "action": 2
        }, {
            "resource": "serviceinstance",
            "action": 2
        }, {
            "resource": "wexp:storefront",
            "action": 2
        }, {
            "resource": "wexp:push:devices:ec0ebb7e56f6454e86c62299a7b32e21",
            "action": 15
        }, {
            "resource": "friends:ec0ebb7e56f6454e86c62299a7b32e21",
            "action": 15
        }]
    })
