"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

verify if a token is valid
"""
import jwt
import sanic
import datetime
from utils.utils import authorized as auth, public_key

from utils.sanic_gzip import Compress

compress = Compress()
verify = sanic.Blueprint("account_verify")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/Account%20Service/account/api/oauth/verify.md
@verify.route("/api/oauth/verify", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def verify_auth(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    verify game auth
    :param request: The request object
    :return: The response object
    """
    if request.headers.get("Authorization", "").startswith("basic "):
        token = jwt.decode(request.headers.get("Authorization", "").replace("basic ", "").replace("eg1~", ""),
                           public_key,
                           algorithms=["RS256"], leeway=20)
        # yes, i know this should be handled by the middleware, but it isn't with the compression :(
        if request.args.get("includePerms"):
            return sanic.response.json({
                "token": f"{request.token}",
                "session_id": token["jti"],
                "token_type": "basic",
                "client_id": token["clid"],
                "internal_client": token["ic"],
                "client_service": token["clsvc"],
                "expires_in": token["exp"] - token["iat"],
                "expires_at": datetime.datetime.fromtimestamp(token["exp"]).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "auth_method": token["am"],
                "app": token["clsvc"],
                "perms": [{
                    "resource": "wexp:cloudstorage:system",
                    "action": 2  # READ
                }, {
                    "resource": "account:public:account:*",
                    "action": 2  # READ
                }, {
                    "resource": "account:oauth:exchangeTokenCode",
                    "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
                }, {
                    "resource": "account:public:account",
                    "action": 2  # READ
                }, {
                    "resource": "priceengine:shared:offer:price",
                    "action": 2  # READ
                }, {
                    "resource": "wexp:wexp_role:client",
                    "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
                }, {
                    "resource": "account:public:account:externalAuths",
                    "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
                }, {
                    "resource": "wexp:calendar",
                    "action": 2  # READ
                }, {
                    "resource": "account:token:otherSessionsForAccountClient",
                    "action": 8  # DELETE
                }, {
                    "resource": "account:token:otherSessionsForAccountClientService",
                    "action": 8  # DELETE
                }, {
                    "resource": "account:public:account:deviceAuths",
                    "action": 11  # CREATE, READ, DELETE
                }, {
                    "resource": "wexp:cloudstorage:system:*",
                    "action": 2  # READ
                }, {
                    "resource": "serviceinstance",
                    "action": 2  # READ
                }, {
                    "resource": "wexp:storefront",
                    "action": 2  # READ
                }]
            })
        return sanic.response.json({
            "token": f"{request.token}",
            "session_id": token["jti"],
            "token_type": "basic",
            "client_id": token["clid"],
            "internal_client": token["ic"],
            "client_service": token["clsvc"],
            "expires_in": token["exp"] - token["iat"],
            "expires_at": datetime.datetime.fromtimestamp(token["exp"]).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "auth_method": token["am"],
            "app": token["clsvc"]
        })
    token = jwt.decode(request.headers.get("Authorization", "").replace("bearer ", "").replace("eg1~", ""),
                       public_key,
                       algorithms=["RS256"], leeway=20)
    if request.args.get("includePerms"):
        return sanic.response.json({
            "token": f"{request.token}",
            "session_id": token["jti"],
            "token_type": "bearer",
            "client_id": token["clid"],
            "internal_client": token["ic"],
            "client_service": token["clsvc"],
            "account_id": token["sub"],
            "expires_in": token["exp"] - token["iat"],
            "expires_at": datetime.datetime.fromtimestamp(token["exp"]).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "auth_method": token["am"],
            "display_name": token["dn"],
            "app": token["clsvc"],
            "in_app_id": token["sub"],
            "device_id": token["dvid"],
            "perms": [{
                "resource": f"blockList:{token['sub']}",
                "action": 14  # READ, UPDATE, DELETE
            }, {
                "resource": "wexp:cloudstorage:system",
                "action": 2  # READ
            }, {
                "resource": "account:public:account:*",
                "action": 2  # READ
            }, {
                "resource": "account:oauth:exchangeTokenCode",
                "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
            }, {
                "resource": "account:public:account",
                "action": 2  # READ
            }, {
                "resource": "priceengine:shared:offer:price",
                "action": 2  # READ
            }, {
                "resource": f"xmpp:session:*:{token['sub']}",
                "action": 1  # CREATE
            }, {
                "resource": "wexp:wexp_role:client",
                "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
            }, {
                "resource": f"wexp:profile:{token['sub']}:*",
                "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
            }, {
                "resource": "account:public:account:externalAuths",
                "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
            }, {
                "resource": "wexp:calendar",
                "action": 2  # READ
            }, {
                "resource": "account:token:otherSessionsForAccountClient",
                "action": 8  # DELETE
            }, {
                "resource": "account:token:otherSessionsForAccountClientService",
                "action": 8  # DELETE
            }, {
                "resource": "account:public:account:deviceAuths",
                "action": 11  # CREATE, READ, DELETE
            }, {
                "resource": "wexp:cloudstorage:system:*",
                "action": 2  # READ
            }, {
                "resource": "serviceinstance",
                "action": 2  # READ
            }, {
                "resource": "wexp:storefront",
                "action": 2  # READ
            }, {
                "resource": f"wexp:push:devices:{token['sub']}",
                "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
            }, {
                "resource": f"friends:{token['sub']}",
                "action": 15  # ALL (CREATE, READ, UPDATE, DELETE)
            }]
        })
    return sanic.response.json({
        "token": f"{request.token}",
        "session_id": token["jti"],
        "token_type": "bearer",
        "client_id": token["clid"],
        "internal_client": token["ic"],
        "client_service": token["clsvc"],
        "account_id": token["sub"],
        "expires_in": token["exp"] - token["iat"],
        "expires_at": datetime.datetime.fromtimestamp(token["exp"]).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "auth_method": token["am"],
        "display_name": token["dn"],
        "app": token["clsvc"],
        "in_app_id": token["sub"],
        "device_id": token["dvid"]
    })
