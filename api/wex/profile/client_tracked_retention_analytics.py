"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles tracking level milestones
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_client_tracked_retention_analytics = sanic.Blueprint("wex_profile_client_tracked_retention_analytics")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ClientTrackedRetentionAnalytics.md
@wex_profile_client_tracked_retention_analytics.route("/<accountId>/ClientTrackedRetentionAnalytics", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def client_tracked_retention_analytics(request: sanic.request.Request,
                                             accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to track account level milestones (either for the level 20/50 fortnite promotions,
    or analytics)
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    current_level = await request.ctx.profile.get_stat("level", request.ctx.profile_id)
    await request.ctx.profile.modify_stat("last_reported_account_level_milestone", current_level,
                                          request.ctx.profile_id)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
