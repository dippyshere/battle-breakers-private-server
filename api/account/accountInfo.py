"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account endpoint
"""
import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
account_info = sanic.Blueprint("account_info")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/Account%20Service/account/api/public/account/accountId.md
@account_info.route("/api/public/account/<accountId>", methods=["GET"])
@auth
@compress.compress()
async def account_route(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Get account info
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    if not request.ctx.is_owner:
        try:
            account_info = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
            return sanic.response.json({
                "id": account_info["id"],
                "displayName": account_info["displayName"],
                "minorVerified": account_info["minorVerified"],
                "minorStatus": account_info["minorStatus"],
                "cabinedMode": account_info["cabinedMode"],
                "externalAuths": account_info["externalAuths"]
            })
        except FileNotFoundError:
            raise errors.com.epicgames.account.account_not_found(accountId)
    account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    return sanic.response.json({
        "id": account["id"],
        "displayName": account["displayName"],
        "minorVerified": account["minorVerified"],
        "minorStatus": account["minorStatus"],
        "cabinedMode": account["cabinedMode"],
        "name": account["name"],
        "email": account["email"],
        "failedLoginAttempts": account["failedLoginAttempts"],
        "lastLogin": account["lastLogin"],
        "numberOfDisplayNameChanges": account["numberOfDisplayNameChanges"],
        "dateOfBirth": account["dateOfBirth"],
        "ageGroup": account["ageGroup"],
        "headless": account["headless"],
        "country": account["country"],
        "lastName": account["lastName"],
        "phoneNumber": account["phoneNumber"],
        "preferredLanguage": account["preferredLanguage"],
        "lastDisplayNameChange": account["lastDisplayNameChange"],
        "canUpdateDisplayName": account["canUpdateDisplayName"],
        "tfaEnabled": account["tfaEnabled"],
        "emailVerified": account["emailVerified"],
        "minorExpected": account["minorExpected"],
        "hasHashedEmail": account["hasHashedEmail"],
        "externalAuths": account["externalAuths"]
    })
