"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account metadata endpoints
"""
import sanic

from utils.exceptions import errors
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
    account = await request.app.ctx.database["accounts"].find_one({"_id": accountId})
    if not account:
        raise errors.com.epicgames.account.account_not_found()
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
        account = await request.app.ctx.database["accounts"].find_one({"_id": accountId}, {"metadata": 1})
        if account and "metadata" in account:
            metadata = account["metadata"]
            try:
                return sanic.response.text(metadata.get(key, ""))
            except KeyError:
                raise errors.com.epicgames.account.metadata_key_not_found()
        else:
            raise errors.com.epicgames.account.metadata_key_not_found()
    else:
        update_result = await request.app.ctx.database["accounts"].update_one(
            {"_id": accountId, f"metadata.{key}": {"$exists": True}},
            {"$unset": {f"metadata.{key}": 1}}
        )
        if update_result.modified_count == 0:
            raise errors.com.epicgames.account.metadata_key_not_found()
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
    account = await request.app.ctx.database["accounts"].find_one({"_id": accountId})
    if not account:
        raise errors.com.epicgames.account.account_not_found()
    if "metadata" not in account:
        account["metadata"] = {}
    if len(account["metadata"]) > 1000:
        raise errors.com.epicgames.account.metadata.too_many_keys()
    account["metadata"][request.json.get("key")] = request.json.get("value")
    await request.app.ctx.database["accounts"].update_one(
        {"_id": accountId},
        {"$set": {"metadata": account["metadata"]}}
    )
    return sanic.response.empty()
