"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the device auth creation for mobile
"""
import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
device_auth = sanic.Blueprint("device_auth")


# undocumented
@device_auth.route("/api/public/account/<accountId>/deviceAuth", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def device_auth_create(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Create a device auth for the account
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    device_authorisation = {
        "deviceId": await request.app.ctx.token_generator(),
        "accountId": accountId,
        "secret": (await request.app.ctx.token_generator()).upper(),
        "userAgent": request.headers.get("User-Agent"),
        "created": {
            "location": None,
            "ipAddress": request.ip,
            "dateTime": await request.app.ctx.format_time()
        }
    }
    account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    account["extra"]["deviceAuths"].append(device_authorisation)
    await request.app.ctx.write_file(f"res/account/api/public/account/{accountId}.json", account)
    return sanic.response.json(device_authorisation)


# undocumented
@device_auth.route("/api/public/account/<accountId>/deviceAuth", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def device_auth_get(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Gets a list of all registered device auths for an account
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    return sanic.response.json(account["extra"]["deviceAuths"])


# undocumented
@device_auth.route("/api/public/account/<accountId>/deviceAuth/<deviceId>", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def device_auth_info(request: sanic.request.Request, accountId: str,
                           deviceId: str) -> sanic.response.JSONResponse:
    """
    Gets info about the specified device auth for an account
    :param request: The request object
    :param accountId: The account id
    :param deviceId: The device id
    :return: The response object
    """
    account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    for device in account["extra"]["deviceAuths"]:
        if device["deviceId"] == deviceId:
            return sanic.response.json(device)
    raise sanic.exceptions.NotFound("Device auth not found")


# undocumented
@device_auth.route("/api/public/account/<accountId>/deviceAuth/<deviceId>", methods=["DELETE"])
@auth(strict=True)
@compress.compress()
async def device_auth_deletion(request: sanic.request.Request, accountId: str,
                               deviceId: str) -> sanic.response.HTTPResponse:
    """
    Remove a device auth for the account
    :param request: The request object
    :param accountId: The account id
    :param deviceId: The device id
    :return: The response object
    """
    account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    for device in account["extra"]["deviceAuths"]:
        if device["deviceId"] == deviceId:
            account["extra"]["deviceAuths"].remove(device)
            break
    await request.app.ctx.write_file(f"res/account/api/public/account/{accountId}.json", account)
    return sanic.response.empty()
