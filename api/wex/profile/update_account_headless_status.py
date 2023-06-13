"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles update headless mcp
"""
import sanic

from utils.sanic_gzip import Compress
from utils.utils import authorized as auth

compress = Compress()
wex_update_headless = sanic.Blueprint("wex_update_headless")


# undocumented
@wex_update_headless.route("/<accountId>/UpdateAccountHeadlessStatus", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def update_headless(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to set the display name on an account and mark it as non-headless.
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: Determine what the request provides us with
    await request.ctx.profile.modify_stat("is_headless", False, request.ctx.profile_id)
    data = await request.app.ctx.read_file(f"res/account/api/public/account/{accountId}.json")
    data["headless"] = False
    await request.app.ctx.write_file(f"res/account/api/public/account/{accountId}.json", data)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
