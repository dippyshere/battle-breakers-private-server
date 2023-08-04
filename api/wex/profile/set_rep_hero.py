"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles setting friend hero
"""

import sanic

from utils.sanic_gzip import Compress
from utils.utils import authorized as auth

compress = Compress()
wex_profile_set_rep_hero = sanic.Blueprint("wex_profile_set_rep_hero")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/SetRepHero.md
@wex_profile_set_rep_hero.route("/<accountId>/SetRepHero", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def set_rep_hero(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to update the player's rep hero
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # if not request.json.get("heroId").startswith("Character:"):
    #     raise errors.com.epicgames.world_explorers.bad_request(errorMessage="Invalid character item id")
    # should probably verify the player's treasure hunter ownership here
    hero_id = request.json.get("heroId")
    slot_index = request.json.get("slotIdx")
    rep_heros = await request.ctx.profile.get_stat("rep_hero_ids")
    if len(rep_heros) <= slot_index:
        rep_heros.append(hero_id)
    else:
        rep_heros[slot_index] = hero_id
    await request.ctx.profile.modify_stat("rep_hero_ids", rep_heros)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
