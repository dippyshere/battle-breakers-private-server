"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles upgrading hero skills.
"""

import sanic

from utils.enums import ProfileType
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_upgrade_hero_skills = sanic.Blueprint("wex_profile_upgrade_hero_skills")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpgradeHeroSkills.md
@wex_profile_upgrade_hero_skills.route("/<accountId>/UpgradeHeroSkills", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def upgrade_hero_skills(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to upgrade hero skills
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: validation
    skill_xp_id = (await request.ctx.profile.find_item_by_template_id("Currency:SkillXP"))[0]
    skill_xp_quantity = (await request.ctx.profile.get_item_by_guid(skill_xp_id))["quantity"]
    await request.ctx.profile.change_item_quantity(skill_xp_id, skill_xp_quantity - request.json.get("xpToSpend"))
    if request.json.get("bIsInPit"):
        hero_data = await request.ctx.profile.get_item_by_guid(request.json.get("heroItemId"), ProfileType.MONSTERPIT)
        await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "skill_level",
                                                        hero_data["attributes"]["skill_level"] + 1,
                                                        ProfileType.MONSTERPIT)
    else:
        hero_data = await request.ctx.profile.get_item_by_guid(request.json.get("heroItemId"), request.ctx.profile_id)
        await request.ctx.profile.change_item_attribute(request.json.get("heroItemId"), "skill_level",
                                                        hero_data["attributes"]["skill_level"] + 1)
    # TODO: investigate skill xp attribute
    await request.ctx.profile.add_notifications({
        "type": "CharacterSkillLevelUp",
        "primary": False,
        "itemId": request.json.get("heroItemId"),
        "level": hero_data["attributes"]["skill_level"] + 1
    }, request.ctx.profile_id)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions, True)
    )
