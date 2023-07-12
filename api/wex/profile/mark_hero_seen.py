"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles marking a hero as seen
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_mark_hero_seen = sanic.Blueprint("wex_profile_mark_hero_seen")


# undocumented
@wex_profile_mark_hero_seen.route("/<accountId>/MarkHeroSeen", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def mark_hero_seen(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used in older versions of the game to mark a hero as seen. It's deprecated and replaced by item
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "is_new", False,
                                                    request.ctx.profile_id)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
