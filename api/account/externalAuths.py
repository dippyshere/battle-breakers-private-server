"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the external auths endpoint
"""
import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
external_auths = sanic.Blueprint("account_external_auths")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/Account%20Service/account/api/public/account/accountId/externalAuths.md
@external_auths.route("/api/public/account/<accountId>/externalAuths", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def external_auth(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Get external auths
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    data = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    if data["externalAuths"] != {}:
        return sanic.response.json([data["externalAuths"]])
    return sanic.response.json([])


# undocumented
@external_auths.route("/api/public/account/<accountId>/externalAuths", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def add_external_auth(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Adds an external auth to an account.
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    data = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    # not bothered to add ALL of the external auths, only adding google cause mobile (fb blocked insecure sign in)
    if request.json["authType"] == "google_user_id":
        data["externalAuths"]["google"] = {
            "accountId": accountId,
            "type": "google",
            "externalAuthId": request.json["externalAuthToken"],
            "externalAuthIdType": "google_user_id",
            "externalDisplayName": "",
            "authIds": [
                {
                    "id": request.json["externalAuthToken"],
                    "type": "google_user_id"
                }
            ]
        }
    else:
        raise errors.com.epicgames.account.ext_auth.unknown_external_auth_type()
    await request.app.ctx.save_file(f"res/account/api/public/account/{accountId}.json", data)
    return sanic.response.json([data["externalAuths"]])


# undocumented
@external_auths.route("/api/public/account/<accountId>/externalAuths/<type>", methods=["GET", "DELETE"])
@auth(strict=True)
@compress.compress()
async def manage_external_auth(request: sanic.request.Request, accountId: str,
                               type: str) -> sanic.response.JSONResponse | sanic.response.HTTPResponse:
    """
    Manage external auths by type
    :param request: The request object
    :param accountId: The account id
    :param type: The external auth type
    :return: The response object
    """
    if request.method == "GET":
        data = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
        for external_auth_accounts in data["externalAuths"]:
            if external_auth_accounts["type"] == type:
                return sanic.response.json(external_auth_accounts)
        raise errors.com.epicgames.account.ext_auth.unknown_external_auth_type()
    elif request.method == "DELETE":
        data = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
        for external_auth_accounts in data["externalAuths"]:
            if external_auth_accounts["type"] == type:
                del data["externalAuths"][external_auth_accounts]
                await request.app.ctx.save_file(f"res/account/api/public/account/{accountId}.json", data)
                return sanic.response.empty()
        raise errors.com.epicgames.account.ext_auth.unknown_external_auth_type()
