"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles removing a hero from the monster pit
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_remove_from_monster_pit = sanic.Blueprint("wex_profile_remove_from_monster_pit")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/RemoveFromMonsterPit.md
@wex_profile_remove_from_monster_pit.route("/<accountId>/RemoveFromMonsterPit", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def remove_from_monster_pit(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to remove a hero from the monster pit
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    mtx_item_id = (await request.ctx.profile.find_item_by_template_id("Currency:MtxGiveaway"))[0]
    mtx_quantity = (await request.ctx.profile.get_item_by_guid(mtx_item_id))["quantity"]
    if mtx_quantity < 50:  # TODO: dont hardcode this value
        raise errors.com.epicgames.modules.gamesubcatalog.purchase_not_allowed(
            errorMessage="Cannot afford to remove item")
    await request.ctx.profile.change_item_quantity(mtx_item_id, mtx_quantity - 50)
    character_item_id = request.json.get("characterItemId")
    character = await request.ctx.profile.get_item_by_guid(character_item_id, request.ctx.profile_id)
    await request.ctx.profile.remove_item(character_item_id, request.ctx.profile_id)
    await request.ctx.profile.add_item(character, character_item_id)
    # This isnt done on the original server, but imo it should be
    await request.ctx.profile.change_item_attribute(character_item_id, "is_new", True)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
