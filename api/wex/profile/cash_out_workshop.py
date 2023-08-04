"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles workshop cash out
"""

import sanic

from utils.sanic_gzip import Compress
from utils.utils import authorized as auth

compress = Compress()
wex_profile_cash_out_workshop = sanic.Blueprint("wex_profile_cash_out_workshop")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/CashOutWorkshop.md
@wex_profile_cash_out_workshop.route("/<accountId>/CashOutWorkshop", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def cash_out_workshop(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to exchange workshop stars to gold
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: validation
    stars = await request.ctx.profile.get_stat("num_levels_completed")
    if stars > 999:
        stars = 999
    gold_id = (await request.ctx.profile.find_item_by_template_id("Currency:Gold"))[0]
    current_gold = (await request.ctx.profile.get_item_by_guid(gold_id))["quantity"]
    workshop_id = (await request.ctx.profile.find_item_by_template_id("HqBuilding:HQ_AncientFactory"))[0]
    workshop_level = (await request.ctx.profile.get_item_by_guid(workshop_id))["attributes"]["level"]
    exchange_rate = \
        (await request.app.ctx.load_datatable("Content/Menus/Headquarters/HQ_AncientFactory"))[0]["Properties"][
            "LaborToGoldExchangeRate"][workshop_level]
    # print(f"Stars: {stars}, Gold: {current_gold}, Workshop Level: {workshop_level}, Exchange Rate: {exchange_rate}")
    await request.ctx.profile.modify_stat("labor_force", {
        "lastInterval": await request.app.ctx.format_time(await request.app.ctx.get_current_12_hour_interval()),
        "laborUsed": stars})
    # await request.ctx.profile.modify_stat("labor_refill_cd",
    #                                       await request.app.ctx.format_time(
    #                                           datetime.datetime.utcnow() + datetime.timedelta(hours=2)))
    await request.ctx.profile.change_item_quantity(gold_id, current_gold + (stars * exchange_rate))
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
