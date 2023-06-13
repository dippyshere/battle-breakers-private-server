"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles suggestion responses.
"""
import os

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_suggestion_response = sanic.Blueprint("wex_profile_suggestion_response")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SuggestionResponse.md
@wex_profile_suggestion_response.route("/<accountId>/SuggestionResponse", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def suggestion_response(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to respond to friend suggestions
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    accounts_list = os.listdir("res/account/api/public/account")
    accounts_list = [account.split(".")[0] for account in accounts_list]
    for friend_id in request.json.get("invitedFriendInstanceIds"):
        friend_instance = await request.ctx.profile.get_item_by_guid(friend_id, request.ctx.profile_id)
        if friend_instance["attributes"].get("status") == "SuggestedLegacy" and friend_instance["attributes"].get(
                "accountId") not in accounts_list:
            raise sanic.exceptions.SanicException("Friend not on private server", 410, quiet=True,
                                                  context={
                                                      "errorMessage": "Unfortunately, this friend has not imported "
                                                                      "their saved account to the private server. "
                                                                      "Mew should ask them to do so :)"
                                                  })
        else:
            await request.ctx.profile.remove_item(friend_id, request.ctx.profile_id)
    for friend_id in request.json.get("rejectedFriendInstanceIds"):
        # TODO: add ignored suggestion list
        await request.ctx.profile.remove_item(friend_id, request.ctx.profile_id)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
