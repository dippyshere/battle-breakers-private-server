"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles unlocking weapon gear.
"""

import sanic

from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_unlock_weapon_gear = sanic.Blueprint("wex_profile_unlock_weapon_gear")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/UnlockWeaponGear.md
@wex_profile_unlock_weapon_gear.route("/<accountId>/UnlockWeaponGear", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def unlock_weapon_gear(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to unlock weapon gear
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: validation
    hero_item = await request.ctx.profile.get_item_by_guid(request.json.get("heroItemId"))
    if not hero_item.get("templateId").startswith("Character:"):
        raise errors.com.epicgames.world_explorers.bad_request(errorMessage="Invalid character item id")
    hero_data = await request.app.ctx.load_character_data(hero_item["templateId"])
    consumed_items = (await request.app.ctx.load_datatable((await request.app.ctx.load_datatable(
        hero_data[0]["Properties"]["HeroGearInfo"]["AssetPathName"].replace("/Game/", "Content/").split(".")[0]))[0][
                                                               "Properties"]["HeroGearSlotRecipe"][
                                                               "ObjectPath"].replace("WorldExplorers/", "").split(".")[
                                                               0]))[0]["Properties"]["ConsumedItems"]
    for consumed_item in consumed_items:
        match consumed_item.get("ItemDefinition", "").get("ObjectName"):
            case "WExpGenericAccountItemDefinition'Reagent_Misc_CeremonialSword'":
                consumed_item_guid = await request.ctx.profile.find_item_by_template_id("Reagent:Reagent_Misc_CeremonialSword")
            case "WExpGenericAccountItemDefinition'Reagent_Misc_CeremonialShield'":
                consumed_item_guid = await request.ctx.profile.find_item_by_template_id("Reagent:Reagent_Misc_CeremonialShield")
            case "WExpGenericAccountItemDefinition'Reagent_Shared_MysteryGoo'":
                consumed_item_guid = await request.ctx.profile.find_item_by_template_id("Reagent:Reagent_Shared_MysteryGoo")
            case _:
                raise errors.com.epicgames.world_explorers.bad_request(errorMessage="Invalid consumed item")
        current_quantity = await request.ctx.profile.get_item_by_guid(consumed_item_guid)["quantity"]
        if current_quantity < consumed_item["Count"]:
            raise errors.com.epicgames.world_explorers.bad_request(errorMessage="Not enough consumed item")
        await request.ctx.profile.update_item_quantity(consumed_item_guid, current_quantity - consumed_item["Count"])
    await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "weapon_unlocked", False)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
