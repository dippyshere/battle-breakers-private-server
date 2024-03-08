"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles claiming account level up rewards etc
"""

import sanic

from utils import types
from utils.enums import AccountPerk
from utils.exceptions import errors
from utils.utils import authorized as auth, get_path_from_template_id

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_claim_account_reward = sanic.Blueprint("wex_profile_claim_account_reward")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/game/v2/profile/accountId/ClaimAccountReward.md
@wex_profile_claim_account_reward.route("/<accountId>/ClaimAccountReward", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def claim_account_reward(request: types.BBProfileRequest, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to claim account level up rewards
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    # TODO: validation
    account_perks = await request.ctx.profile.get_stat("account_perks")
    rewards_claimed = await request.ctx.profile.get_stat("rewards_claimed")
    perk_quantities = {}
    for perk in request.json.get("perks"):
        perk_item = await request.ctx.profile.get_item_by_guid(perk.get("itemId"))
        if perk_item is None or not perk_item["templateId"].startswith("AccountReward:"):
            raise errors.com.epicgames.world_explorers.bad_request(errorMessage=f"Invalid perk {perk['templateId']}")
        perk_data = (await get_path_from_template_id(perk_item["templateId"]))[0]["Properties"]
        if perk.get("perkChoice") == 0:
            perk_choice = AccountPerk.from_string(perk_data["ChoiceA"])
        elif perk.get("perkChoice") == 1:
            perk_choice = AccountPerk.from_string(perk_data["ChoiceB"])
        else:
            raise errors.com.epicgames.world_explorers.bad_request(
                errorMessage=f"Invalid perk choice {perk['perkChoice']}")
        if perk.get("itemId") not in perk_quantities:
            perk_quantities[perk.get("itemId")] = perk_item["quantity"]
        perk_quantities[perk.get("itemId")] -= 1
        if perk_quantities[perk.get("itemId")] == 0:
            await request.ctx.profile.remove_item(perk.get("itemId"))
        if perk_quantities[perk.get("itemId")] > 0:
            continue
        await request.ctx.profile.change_item_quantity(perk.get("itemId"), perk_quantities[perk.get("itemId")])
        rewards_claimed[perk_item["templateId"]] += 1
        match perk_choice:
            case AccountPerk.MaxMana:
                account_perks["MaxMana"] += 1
            case AccountPerk.DamageReduction:
                account_perks["DamageReduction"] += 1
            case AccountPerk.SpecialAttack:
                account_perks["SpecialAttack"] += 1
            case AccountPerk.Attack:
                account_perks["Attack"] += 1
            case AccountPerk.BasicAttack:
                account_perks["BasicAttack"] += 1
            case AccountPerk.PetStrength:
                account_perks["PetStrength"] += 1
            case AccountPerk.RegenStat:
                account_perks["RegenStat"] += 1
            case AccountPerk.MaxHitPoints:
                account_perks["MaxHitPoints"] += 1
    await request.ctx.profile.set_stat("account_perks", account_perks)
    await request.ctx.profile.set_stat("rewards_claimed", rewards_claimed)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
