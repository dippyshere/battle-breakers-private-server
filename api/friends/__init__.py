"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the friend requests
"""
import sanic

from utils.friend_system import PlayerFriends
from .summary import summary
from .friend_requests import friend_request
from .settings import settings
from .version import friends_version

friends = sanic.Blueprint.group(summary, friends_version, friend_request, url_prefix="/friends")


@friends.on_request
async def add_friends_profile(request: sanic.request.Request) -> None:
    """
    Adds the friends service data to the request context for use in the handlers
    :param request: The request object
    :return: None
    """
    account_id = request.match_info.get('accountId')
    if account_id is not None:
        if account_id not in request.app.ctx.friends:
            request.app.ctx.friends[account_id] = await PlayerFriends.init_friends(account_id)
        request.ctx.friends = request.app.ctx.friends[account_id]
    else:
        request.ctx.friends = None
