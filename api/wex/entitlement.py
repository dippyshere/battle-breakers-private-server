"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles entitlement check
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth, uuid_generator, read_file, write_file, format_time

wex_entitlement = sanic.Blueprint("wex_entitlement")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/entitlementCheck.md
@wex_entitlement.route("/api/entitlementCheck", methods=["GET"])
@auth
async def entitlement_check(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to check if the user has access to the game, and if not, grant them (probably).
    :param request: The request object
    :return: The response object (204)
    """
    entitlements = await read_file(f"res/entitlement/api/account/{request.ctx.owner}.json")
    for entitlement in entitlements:
        if entitlement.get("catalogItemId") == "e458e71024404176addca212860f9ef2":
            return sanic.response.empty()
    raise errors.com.epicgames.common.missing_action("PLAY")


@wex_entitlement.route("/api/storeaccess/v1/request_access/<accountId>", methods=["POST"])
@auth(strict=True)
async def request_access(request: sanic.request.Request, accountId: str) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to request free access to the game.
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    entitlements = await read_file(f"res/entitlement/api/account/{request.ctx.owner}.json")
    for entitlement in entitlements:
        if entitlement.get("catalogItemId") == "e458e71024404176addca212860f9ef2":
            raise sanic.exceptions.BadRequest(context={"errorMessage": "Already have access to this game."})
    entitlements.append({
        "id": await uuid_generator(),
        "entitlementName": "WorldExplorers_Free",
        "namespace": "wex",
        "catalogItemId": "e458e71024404176addca212860f9ef2",
        "accountId": request.ctx.owner,
        "identityId": request.ctx.owner,
        "entitlementType": "AUDIENCE",
        "grantDate": await format_time(),
        "consumed": False,
        "status": "ACTIVE",
        "active": True,
        "useCount": 0,
        "originalUseCount": 0,
        "platformType": "EPIC",
        "created": "2019-11-08T10:47:00.476Z",
        "updated": "2019-11-08T10:47:00.476Z",
        "groupEntitlement": False,
        "country": None
    })
    await write_file(f"res/entitlement/api/account/{request.ctx.owner}.json", entitlements)
    return sanic.response.empty()
    # TODO Check for bans
    # raise errors.com.epicgames.world_explorers.banned_access_found_when_granting()
    # raise errors.com.epicgames.bad_request(
    #     errorMessage = "Client requested access grant but has banned access entitlement.",
    #     numericErrorCode = 1001
    # )


@wex_entitlement.route("/api/storeaccess/v1/redeem_access/<accountId>", methods=["POST"])
@auth(strict=True)
async def redeem_access(request: sanic.request.Request, accountId: str) -> sanic.response.HTTPResponse:
    """
    This endpoint is used to redeem access to the game.
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    entitlements = await read_file(f"res/entitlement/api/account/{request.ctx.owner}.json")
    for entitlement in entitlements:
        if entitlement.get("catalogItemId") == "e458e71024404176addca212860f9ef2":
            raise sanic.exceptions.BadRequest(context={"errorMessage": "Already have access to this game."})
    entitlements.append({
        "id": await uuid_generator(),
        "entitlementName": "WorldExplorers_Free",
        "namespace": "wex",
        "catalogItemId": "e458e71024404176addca212860f9ef2",
        "accountId": request.ctx.owner,
        "identityId": request.ctx.owner,
        "entitlementType": "AUDIENCE",
        "grantDate": await format_time(),
        "consumed": False,
        "status": "ACTIVE",
        "active": True,
        "useCount": 0,
        "originalUseCount": 0,
        "platformType": "EPIC",
        "created": "2019-11-08T10:47:00.476Z",
        "updated": "2019-11-08T10:47:00.476Z",
        "groupEntitlement": False,
        "country": None
    })
    await write_file(f"res/entitlement/api/account/{request.ctx.owner}.json", entitlements)
    return sanic.response.empty()
    # TODO Check for bans
    # raise errors.com.epicgames.world_explorers.banned_access_found_when_granting()


@wex_entitlement.route("/api/accesscontrol/status", methods=["GET"])
@auth
async def real_game_access(request: sanic.request.Request, accountId: str) -> sanic.response.HTTPResponse:
    """
    This endpoint is used for something, who knows
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    entitlements = await read_file(f"res/entitlement/api/account/{request.ctx.owner}.json")
    for entitlement in entitlements:
        if entitlement.get("catalogItemId") == "e458e71024404176addca212860f9ef2":
            return sanic.response.json({
                "play": True,
                "isBanned": False,
            })
    # TODO: Check for bans
    raise errors.com.epicgames.common.missing_action("PLAY")
