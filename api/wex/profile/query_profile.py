"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles profile queries
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_query = sanic.Blueprint("wex_profile_query")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/QueryProfile(profile0).md
@wex_profile_query.route("/<accountId>/QueryProfile", methods=["GET", "POST"])
@auth(strict=True)
@compress.compress()
async def query_profile(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Handles the query profile request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
