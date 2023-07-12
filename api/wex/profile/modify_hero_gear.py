"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles modifying hero gear.
"""

import sanic

from utils.enums import ProfileType
from utils.exceptions import errors
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_modify_hero_gear = sanic.Blueprint("wex_profile_modify_hero_gear")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/ModifyHeroGear.md
# noinspection IncorrectFormatting
@wex_profile_modify_hero_gear.route("/<accountId>/ModifyHeroGear", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def modify_hero_gear(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to modify hero gear.
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    if request.json.get("bIsInPit"):
        if not (await request.ctx.profile.get_item_by_guid(request.json.get("heroItemId"), ProfileType.MONSTERPIT))[
                "templateId"].startswith("Character:"):
            raise errors.com.epicgames.world_explorers.bad_request(errorMessage="Invalid hero item id")
    else:
        if not (await request.ctx.profile.get_item_by_guid(request.json.get("heroItemId")))[
                "templateId"].startswith("Character:"):
            raise errors.com.epicgames.world_explorers.bad_request(errorMessage="Invalid hero item id")
    if request.json.get("gearHeroItemId") != "":
        sidekick_template_id = (await request.ctx.profile.get_item_by_guid(request.json.get("gearHeroItemId")))[
                "templateId"]
        if not sidekick_template_id.startswith("Character:"):
            raise errors.com.epicgames.world_explorers.bad_request(errorMessage="Invalid gear weapon item id")
        await request.ctx.profile.change_item_attribute(request.json.get("gearHeroItemId"), "used_as_sidekick", True)
        await request.ctx.profile.change_item_attribute(request.json.get("gearHeroItemId"), "sidekick_item_id",
                                                        request.json.get("heroItemId"))
        if request.json.get("bIsInPit"):
            await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "sidekick_item_id",
                                                            request.json.get("gearHeroItemId"),
                                                            ProfileType.MONSTERPIT)
            await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "sidekick_template_id",
                                                            sidekick_template_id, ProfileType.MONSTERPIT)
        else:
            await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "sidekick_item_id",
                                                            request.json.get("gearHeroItemId"))
            await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "sidekick_template_id",
                                                            sidekick_template_id)
    else:
        await request.ctx.profile.change_item_attribute(request.json.get("gearHeroItemId"), "used_as_sidekick", False)
        await request.ctx.profile.change_item_attribute(request.json.get("gearHeroItemId"), "sidekick_item_id", "")
        if request.json.get("bIsInPit"):
            await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "sidekick_item_id", "",
                                                            ProfileType.MONSTERPIT)
            await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "sidekick_template_id",
                                                            "", ProfileType.MONSTERPIT)
        else:
            await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "sidekick_item_id", "")
            await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "sidekick_template_id", "")
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions, True)
    )
