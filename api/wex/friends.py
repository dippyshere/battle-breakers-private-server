"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the manifest
"""
import sanic

from utils.profile_system import PlayerProfile, ProfileType
from utils.sanic_gzip import Compress

compress = Compress()
wex_friend = sanic.Blueprint("wex_friend")


# undocumented
@wex_friend.route("/api/game/v2/friends/<accountId>/search", methods=['GET'])
@compress.compress()
async def wex_friends_search(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to search for friends
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    account_id = request.match_info.get('accountId')
    if account_id is not None:
        if account_id not in request.app.ctx.profiles:
            request.app.ctx.profiles[account_id] = PlayerProfile(account_id)
        request.ctx.profile = request.app.ctx.profiles[account_id]
    else:
        request.ctx.profile = None
    if request.args.get("rvn") is None:
        request.ctx.rvn = -1
    else:
        try:
            request.ctx.rvn = int(request.args.get("rvn"))
        except:
            request.ctx.rvn = -1
    request.ctx.profile_id = ProfileType.from_string("friends")
    request.ctx.profile_revisions = request.headers.get("X-EpicGames-ProfileRevisions")
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
