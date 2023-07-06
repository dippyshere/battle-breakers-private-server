"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles finalizing levels
"""

import sanic

from utils.exceptions import errors
from utils.enums import ProfileType
from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_finalize_level = sanic.Blueprint("wex_profile_finalize_level")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/FinalizeLevel.md
@wex_profile_finalize_level.route("/<accountId>/FinalizeLevel", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def finalize_level(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to finalize a level upon completion / abandoning
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    try:
        level_notification = await request.ctx.profile.get_notifications(ProfileType.LEVELS)
        level_id = level_notification[0]["level"]["levelId"]
    except:
        try:
            level_item = await request.ctx.profile.get_item_by_guid(
                await request.ctx.profile.find_item_by_template_id("Level:InProgress", request.ctx.profile_id),
                request.ctx.profile_id)
            level_id = level_item["attributes"]["debug_name"]
        except:
            raise errors.com.epicgames.world_explorers.level_not_found(errorMessage="Sorry, the level you completed could not be found.")
    stars = await request.ctx.profile.get_stat("num_levels_completed")
    try:
        difficulty = int(level_id[-1])
    except ValueError:
        difficulty = 1
    await request.ctx.profile.clear_notifications(ProfileType.LEVELS)
    await request.ctx.profile.remove_item(request.json.get("levelItemId"), request.ctx.profile_id)
    for unlocked_level_guids in (await request.ctx.profile.find_item_by_template_id("WorldUnlock:Level",
                                                                                    request.ctx.profile_id)):
        level_item = await request.ctx.profile.get_item_by_guid(unlocked_level_guids, request.ctx.profile_id)
        if level_item["attributes"]["levelId"] == level_id:
            break
    else:
        await request.ctx.profile.add_item({
            "templateId": "WorldUnlock:Level",
            "attributes": {
                "levelId": level_id
            },
            "quantity": 1
        }, profile_id=request.ctx.profile_id)
        await request.ctx.profile.modify_stat("num_levels_completed", stars + difficulty)
    await request.ctx.profile.modify_stat("last_played_level", level_id, profile_id=request.ctx.profile_id)
    level_complete_notification = [
        {
            "type": "WExpLevelCompleted",
            "primary": False,
            "accountXp": 0,
            "bonusAccountXp": 0,
            "levelId": level_id,
            "completed": True,
            "loot": []
        }
    ]
    # TODO: add level loot to the notification
    # TODO: determine if the level was completed or only partially completed
    await request.ctx.profile.add_notifications(level_complete_notification, ProfileType.LEVELS)
    # TODO: update account level + xp + add perk choice + notification
    # TODO: activity gift box
    # TODO: award level loot
    # TODO: update battle pass xp/currency
    # TODO: update score
    # TODO: monserpit unlocks if applicable
    # TODO: LevelRunMarker for limited run rooms
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions, True)
    )
