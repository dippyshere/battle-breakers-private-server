"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles level abandon/exit profile mcp
"""

import sanic

from utils.enums import ProfileType
from utils.utils import authorized as auth, format_time

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_abandon_level = sanic.Blueprint("wex_profile_abandon_level")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/AbandonLevel.md
@wex_profile_abandon_level.route("/<accountId>/AbandonLevel", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def abandon_level(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to abandon the level
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    await request.ctx.profile.modify_stat("last_forgiven_abandon", await format_time(), request.ctx.profile_id)
    await request.ctx.profile.remove_item(request.json.get("levelItemId"), request.ctx.profile_id)
    # TODO: calculate quests + handle rewards for completed rooms
    await request.ctx.profile.clear_notifications(ProfileType.LEVELS)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
