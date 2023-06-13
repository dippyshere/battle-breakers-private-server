"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles updating default party
"""
import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_profile_set_default_party = sanic.Blueprint("wex_profile_set_default_party")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SetDefaultParty.md
@wex_profile_set_default_party.route("/<accountId>/SetDefaultParty", methods=["POST"])
@auth(strict=True)
@compress.compress()
async def set_default_party(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    This endpoint is used to update the default hero party slot
    :param request: The request object
    :param accountId: The account id
    :return: The modified profile
    """
    party_id = request.json.get("partyId")
    party_type = request.json.get("type")
    parties = await request.ctx.profile.get_stat("default_parties", request.ctx.profile_id)
    parties[party_type] = party_id
    parties["LastPvePartyUsed"] = party_id
    # TODO: test compatability with old clients using different party names
    await request.ctx.profile.modify_stat("default_parties", parties, request.ctx.profile_id)
    return sanic.response.json(
        await request.ctx.profile.construct_response(request.ctx.profile_id, request.ctx.rvn,
                                                     request.ctx.profile_revisions)
    )
