"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles friends reconciliation.
"""
import os

import sanic

from utils.friend_system import PlayerFriends
from utils.enums import ProfileType
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_reconcile = sanic.Blueprint("wex_profile_reconcile")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/Reconcile.md
@wex_profile_reconcile.route("/<accountId>/Reconcile", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def reconcile(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to determine whether epic friends have battle breakers or not.
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    await request.ctx.profile.clear_notifications()
    results = {}
    if accountId not in request.app.ctx.friends:
        request.app.ctx.friends[accountId] = PlayerFriends(accountId)
    friends_list = request.json["friendIdList"]
    friends_list.extend(request.json["outgoingIdList"])
    friends_list.extend(request.json["incomingIdList"])
    accounts_list = [acc.split(".")[0] for acc in os.listdir("res/account/api/public/account/")]
    for friend in friends_list:
        if friend in accounts_list:
            results[friend] = True
        else:
            results[friend] = False
    await request.ctx.profile.add_notifications({
        "type": "WExpReconcileNotification",
        "primary": True,
        "results": results
    }, ProfileType.FRIENDS)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions, True)
    )
