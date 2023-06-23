"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account metadata endpoints
"""
import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
account_metadata = sanic.Blueprint("account_metadata")


# undocumented
@account_metadata.route("/api/public/account/<accountId>/metadata", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def get_metadata(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Get all account metadata
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    return sanic.response.json(account.get("metadata", {}))


# undocumented
@account_metadata.route("/api/public/account/<accountId>/metadata/<key>", methods=["GET", "DELETE"])
@auth(strict=True)
@compress.compress()
async def get_delete_metadata(request: sanic.request.Request, accountId: str, key: str) -> sanic.response.HTTPResponse:
    """
    Get/Delete a specific account metadata value
    :param request: The request object
    :param accountId: The account id
    :param key: The metadata key
    :return: The response object
    """
    if request.method == "GET":
        account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
        return sanic.response.text(account.get("metadata", {}).get(key, ""))
    else:
        account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
        if key in account.get("metadata", {}):
            del account["metadata"][key]
            await request.app.ctx.write_file(f"res/account/api/public/account/{accountId}.json", account)
        return sanic.response.empty()


# undocumented
@account_metadata.route("/api/public/account/<accountId>/metadata", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def set_metadata(request: sanic.request.Request, accountId: str) -> sanic.response.HTTPResponse:
    """
    Set a specific account metadata value
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    account = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    if "metadata" not in account:
        account["metadata"] = {}
    account["metadata"][request.json["key"]] = request.json["value"]
    await request.app.ctx.write_file(f"res/account/api/public/account/{accountId}.json", account)
    return sanic.response.empty()
