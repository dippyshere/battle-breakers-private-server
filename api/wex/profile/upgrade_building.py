"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles upgrading buildings.
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_upgrade_building = sanic.Blueprint("wex_profile_upgrade_building")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/UpgradeBuilding.md
@wex_profile_upgrade_building.route("/<accountId>/UpgradeBuilding", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def upgrade_building(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to upgrade buildings
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: modify chest activity
    building_item = await request.ctx.profile.get_item_by_guid(request.json.get("buildingItemId"),
                                                               request.ctx.profile_id)
    if building_item["templateId"].split(":")[0] == "HqBuilding":
        promotion_table = (await request.app.ctx.load_datatable((await request.app.ctx.load_datatable((await request.app.ctx.load_datatable(f"Content/Menus/Headquarters/{building_item['templateId'].split(':')[-1]}"))[0]["Properties"]["PromotionTable"]["ObjectPath"].replace("WorldExplorers/", "").split(".")[0]))[0]["Properties"]["RankRecipes"][building_item["attributes"]["level"]]["AssetPathName"].replace("/Game/", "Content/").split(".")[0]))[0]["Properties"]
        for item in promotion_table["ConsumedItems"]:
            item_template_id = await request.app.ctx.get_template_id_from_path(item["ItemDefinition"]["ObjectPath"])
            current_item = await request.ctx.profile.find_item_by_template_id(item_template_id)
            current_quantity = (await request.ctx.profile.get_item_by_guid(current_item[0]))["quantity"]
            # print("Cost: " + str(item["Count"]) + " " + item_template_id)
            await request.ctx.profile.change_item_quantity(current_item[0],
                                                           current_quantity - item["Count"])
        if promotion_table.get("MtxCost") is not None:
            # TODO: enforce account level
            mtx_item_id = (await request.ctx.profile.find_item_by_template_id("Currency:MtxGiveaway"))[0]
            mtx_quantity = (await request.ctx.profile.get_item_by_guid(mtx_item_id))["quantity"]
            await request.ctx.profile.change_item_quantity(mtx_item_id, mtx_quantity - promotion_table["MtxCost"])
    await request.ctx.profile.change_item_attribute(request.json.get("buildingItemId"), "level",
                                                    building_item["attributes"]["level"] + 1, request.ctx.profile_id)
    # print("Upgraded building " + request.json.get("buildingItemId") + " to level " + str(
    #     building_item["attributes"]["level"] + 1))
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
