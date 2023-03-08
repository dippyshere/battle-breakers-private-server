"""
Handles party update request
"""
import datetime

import orjson
import sanic

wex_profile_update_party = sanic.Blueprint("wex_profile_update_party")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/UpdateParty.md
@wex_profile_update_party.route("/wex/api/game/v2/profile/<accountId>/UpdateParty", methods=["POST"])
async def update_party(request, accountId):
    """
    This endpoint is used to update the party
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    return sanic.response.json({
        "profileRevision": int(int(request.args.get("rvn"))) + 1,
        "profileId": "profile0",
        "profileChangesBaseRevision": int(request.args.get("rvn")),
        "profileChanges": [
            {
                "changeType": "itemAttrChanged",
                "itemId": request.json["partyItemId"],
                "attributeName": "character_ids",
                "attributeValue": request.json["partyInstance"]["character_ids"]
            }
        ],
        "profileCommandRevision": orjson.loads(request.headers.get("X-EpicGames-ProfileRevisions"))[0]["clientCommandRevision"],
        "responseVersion": 1
    }, headers={"X-EpicGames-Profile-Revision": request.args.get('rvn'), "X-EpicGames-MinBuild": 0,
                "X-EpicGames-ContentVersion": "1.88.244-r17036752",
                "X-EpicGames-McpVersion": "prod Release-1.88-1.88 build 107 cl 19310354",
                "X-Epic-Device-ID": "68009daed09498667a8039cce09983ed",
                "X-Epic-Correlation-ID": "UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9"
                                         "-3DCE6A3847C4B8CE865202976E4FE5E3"})
