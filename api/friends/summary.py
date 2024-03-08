"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the friends summary
"""

import sanic

from utils import types
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
summary = sanic.Blueprint("friends_summary")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/Friends%20Service/friends/api/v1/accountId/summary.md
@summary.route("/api/v1/<accountId>/summary", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def friends_summary(request: types.BBFriendRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get friends summary
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json((await request.ctx.friends.get_summary()))


@summary.route("/api/v1/<accountId>/friends", methods=["GET", "DELETE"])
@auth(strict=True)
@compress.compress()
async def friends_list_get_delete(request: types.BBFriendRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get friends summary
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    if request.method == "DELETE":
        for friendId in await request.ctx.friends.get_friends():
            await request.ctx.friends.remove_friend(request, friendId)
    return sanic.response.json((await request.ctx.friends.get_summary())["friends"])


@summary.route("/api/v1/<accountId>/incoming", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def friends_incoming(request: types.BBFriendRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get friends incoming summary
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json((await request.ctx.friends.get_summary())["incoming"])


@summary.route("/api/v1/<accountId>/outgoing", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def friends_outgoing(request: types.BBFriendRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get friends outgoing summary
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json((await request.ctx.friends.get_summary())["outgoing"])


@summary.route("/api/v1/<accountId>/suggested", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def friends_suggested(request: types.BBFriendRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get friends suggested summary
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json((await request.ctx.friends.get_summary())["suggested"])


@summary.route("/api/v1/<accountId>/blocklist", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def friends_blocked(request: types.BBFriendRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get friends blocked list
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json((await request.ctx.friends.get_summary())["blocklist"])


@summary.route("/api/v1/<accountId>/blocklist/<friendId>", methods=["POST", "DELETE"])
@auth(strict=True)
@compress.compress()
async def block_friend(request: types.BBFriendRequest, accountId: str) -> sanic.response.HTTPResponse:
    """
    Get friends blocked list
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    if request.method == "POST":
        friends_list = await request.ctx.friends.get_friends()
        friends_list["blocklist"].append(request.json["friendId"])
        await request.ctx.friends.update_friends(friends_list)
    else:
        friends_list = await request.ctx.friends.get_friends()
        friends_list["blocklist"].remove(request.json["friendId"])
        await request.ctx.friends.update_friends(friends_list)
    return sanic.response.empty()


@summary.route("/api/public/friends/<accountId>", methods=["GET"])
@auth(strict=True)
@compress.compress()
async def legacy_friends_summary(request: types.BBFriendRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get friends summary
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json((await request.ctx.friends.get_legacy_summary()))


@summary.route("/api/public/blocklist/<accountId>", methods=["GET", "DELETE"])
@auth(strict=True)
@compress.compress()
async def friends_legacy_blocklist(request: types.BBFriendRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    Get friends blocklist
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    if request.method == "DELETE":
        friends_list = await request.ctx.friends.get_friends()
        friends_list["blocklist"] = []
        await request.ctx.friends.update_friends(friends_list)
    blocklist = {"blockedUsers": []}
    for friendId in (await request.ctx.friends.get_friends())["blocklist"]:
        blocklist["blockedUsers"].append({"accountId": friendId})
    return sanic.response.json(blocklist)
