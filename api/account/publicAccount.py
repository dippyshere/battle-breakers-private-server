"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the public facing account info endpoint
"""
import urllib.parse

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
public_account = sanic.Blueprint("account_public")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/public/account.md
@public_account.route("/api/public/account", methods=["GET"])
@auth
@compress.compress()
async def public_account_info(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Bulk get account info
    :param request: The request object
    :return: The response object
    """
    if len(request.args.getlist("accountId")) > 100:
        raise errors.com.epicgames.account.invalid_account_id_count(100)
    final_accounts = []
    for accountId in request.args.getlist("accountId"):
        # TODO: handle invalid account ids
        try:
            account_info = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
            final_accounts.append({
                "id": account_info["id"],
                "displayName": account_info["displayName"],
                "minorVerified": account_info["minorVerified"],
                "minorStatus": account_info["minorStatus"],
                "cabinedMode": account_info["cabinedMode"],
                "externalAuths": account_info["externalAuths"]
            })
        except FileNotFoundError:
            pass
    return sanic.response.json(final_accounts)


@public_account.route("/api/public/account/displayName/<displayName>", methods=["GET"])
@auth
@compress.compress()
async def account_displayname(request: sanic.request.Request, displayName: str) -> sanic.response.JSONResponse:
    """
    Get an account by name
    :param request: The request object
    :param displayName: The display name
    :return: The response object
    """
    displayName = urllib.parse.unquote(displayName)
    requested_id = await request.app.ctx.get_account_id_from_display_name(displayName)
    if requested_id is None:
        raise errors.com.epicgames.account.account_not_found(displayName)
    account_info = await request.app.ctx.read_file(f"res/account/api/public/account/{requested_id}.json")
    if requested_id == request.ctx.owner:
        return sanic.response.json({
            "id": account_info["id"],
            "displayName": account_info["displayName"],
            "minorVerified": account_info["minorVerified"],
            "minorStatus": account_info["minorStatus"],
            "cabinedMode": account_info["cabinedMode"],
            "name": account_info["name"],
            "email": account_info["email"],
            "failedLoginAttempts": account_info["failedLoginAttempts"],
            "lastLogin": account_info["lastLogin"],
            "numberOfDisplayNameChanges": account_info["numberOfDisplayNameChanges"],
            "dateOfBirth": account_info["dateOfBirth"],
            "ageGroup": account_info["ageGroup"],
            "headless": account_info["headless"],
            "country": account_info["country"],
            "lastName": account_info["lastName"],
            "phoneNumber": account_info["phoneNumber"],
            "preferredLanguage": account_info["preferredLanguage"],
            "lastDisplayNameChange": account_info["lastDisplayNameChange"],
            "canUpdateDisplayName": account_info["canUpdateDisplayName"],
            "tfaEnabled": account_info["tfaEnabled"],
            "emailVerified": account_info["emailVerified"],
            "minorExpected": account_info["minorExpected"],
            "hasHashedEmail": account_info["hasHashedEmail"],
            "externalAuths": account_info["externalAuths"]
        })
    return sanic.response.json({
        "id": account_info["id"],
        "displayName": account_info["displayName"],
        "minorVerified": account_info["minorVerified"],
        "minorStatus": account_info["minorStatus"],
        "cabinedMode": account_info["cabinedMode"],
        "externalAuths": account_info["externalAuths"]
    })


@public_account.route("/api/public/account/email/<email>", methods=["GET"])
@auth
@compress.compress()
async def account_email(request: sanic.request.Request, email: str) -> sanic.response.JSONResponse:
    """
    Get account by email (deprecated on official API)
    :param request: The request object
    :param email: The email
    :return: The response object
    """
    requested_id = await request.app.ctx.get_account_id_from_email(email)
    if requested_id is None:
        raise errors.com.epicgames.account.account_not_found(email)
    account_info = await request.app.ctx.read_file(f"res/account/api/public/account/{requested_id}.json")
    if requested_id == request.ctx.owner:
        return sanic.response.json({
            "id": account_info["id"],
            "displayName": account_info["displayName"],
            "minorVerified": account_info["minorVerified"],
            "minorStatus": account_info["minorStatus"],
            "cabinedMode": account_info["cabinedMode"],
            "name": account_info["name"],
            "email": account_info["email"],
            "failedLoginAttempts": account_info["failedLoginAttempts"],
            "lastLogin": account_info["lastLogin"],
            "numberOfDisplayNameChanges": account_info["numberOfDisplayNameChanges"],
            "dateOfBirth": account_info["dateOfBirth"],
            "ageGroup": account_info["ageGroup"],
            "headless": account_info["headless"],
            "country": account_info["country"],
            "lastName": account_info["lastName"],
            "phoneNumber": account_info["phoneNumber"],
            "preferredLanguage": account_info["preferredLanguage"],
            "lastDisplayNameChange": account_info["lastDisplayNameChange"],
            "canUpdateDisplayName": account_info["canUpdateDisplayName"],
            "tfaEnabled": account_info["tfaEnabled"],
            "emailVerified": account_info["emailVerified"],
            "minorExpected": account_info["minorExpected"],
            "hasHashedEmail": account_info["hasHashedEmail"],
            "externalAuths": account_info["externalAuths"]
        })
    return sanic.response.json({
        "id": account_info["id"],
        "displayName": account_info["displayName"],
        "minorVerified": account_info["minorVerified"],
        "minorStatus": account_info["minorStatus"],
        "cabinedMode": account_info["cabinedMode"],
        "externalAuths": account_info["externalAuths"]
    })


# undocumented
@public_account.route("/api/public/account/lookup/externalId", methods=["POST"])
@auth()
@compress.compress()
async def external_id_lookup(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Look up accounts by external id
    same response structure as above
    :param request: The request object
    :return: The response object
    """
    raise errors.com.epicgames.not_implemented()


# undocumented
@public_account.route("/api/public/account/lookup/externalAuth/<externalAuthType>/displayName/<displayName>",
                      methods=["GET"])
@auth()
@compress.compress()
async def external_id_lookup_by_name(request: sanic.request.Request, externalAuthType: str,
                                     displayName: str) -> sanic.response.JSONResponse:
    """
    Look up accounts by external id
    same response structure as above
    :param request: The request object
    :param externalAuthType: The external auth type
    :param displayName: The display name
    :return: The response object
    """
    raise errors.com.epicgames.not_implemented()
