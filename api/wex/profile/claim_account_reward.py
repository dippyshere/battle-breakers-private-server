"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles claiming account level up rewards etc
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_claim_account_reward = sanic.Blueprint("wex_profile_claim_account_reward")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ClaimAccountReward.md
@wex_profile_claim_account_reward.route("/<accountId>/ClaimAccountReward", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def claim_account_reward(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to claim account level up rewards
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    raise errors.com.epicgames.not_found()
