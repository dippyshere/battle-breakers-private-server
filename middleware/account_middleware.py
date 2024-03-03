"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

This file contains the middleware for account related endpoints
"""
import sanic.request


async def include_perms(request: sanic.request.Request, response: sanic.response.JSONResponse) -> None:
    """
    Middleware to add perms to the response if requested

    :param request: The request object
    :param response: The response object
    :return: None
    """
    if request.args.get("includePerms") and response.status < 300 and not response._body_manually_set:
        response.update({"perms": [{
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
            "resource": "wexp:wexp_role:client",
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
        }]})
