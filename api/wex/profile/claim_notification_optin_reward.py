"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles claiming the notification opt-in reward
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_claim_notification_opt_in_reward = sanic.Blueprint("wex_profile_claim_notification_opt_in_reward")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/ClaimNotificationOptInReward.md
@wex_profile_claim_notification_opt_in_reward.route("/<accountId>/ClaimNotificationOptInReward", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def claim_notification_opt_in_reward(request: sanic.request.Request,
                                           accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to claim the notification opt-in reward
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    await request.ctx.profile.add_item({
        "templateId": "Giftbox:GB_NotificationOptInReward",
        "attributes": {
            "sealed_days": 0,
            "params": {},
            "min_level": 1
        },
        "quantity": 1
    }, profile_id=request.ctx.profile_id)
    await request.ctx.profile.modify_stat("notification_optin_reward_claimed", True, request.ctx.profile_id)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
