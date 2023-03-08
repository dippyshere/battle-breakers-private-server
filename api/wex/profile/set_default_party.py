"""
Handles updating default party
"""
import orjson
import sanic
import datetime

wex_profile_set_default_party = sanic.Blueprint("wex_profile_set_default_party")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SetDefaultParty.md
@wex_profile_set_default_party.route("/wex/api/game/v2/profile/<accountId>/SetDefaultParty", methods=["POST"])
async def set_default_party(request, accountId):
    """
    This endpoint is used to update the default hero party slot
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    with open(f"res/wex/api/game/v2/profile/{accountId}/QueryProfile/{request.args.get('profileId')}.json", "r", encoding='utf-8') as file:
        profile_query = orjson.loads(file.read())
    PveLight = request.json["partyId"] if request.json["type"] == "PveLight" else profile_query['profileChanges'][0]['profile']['stats']['attributes']['default_parties']['PveLight']
    PveFire = request.json["partyId"] if request.json["type"] == "PveFire" else profile_query['profileChanges'][0]['profile']['stats']['attributes']['default_parties']['PveFire']
    PveDark = request.json["partyId"] if request.json["type"] == "PveDark" else profile_query['profileChanges'][0]['profile']['stats']['attributes']['default_parties']['PveDark']
    PveNature = request.json["partyId"] if request.json["type"] == "PveNature" else profile_query['profileChanges'][0]['profile']['stats']['attributes']['default_parties']['PveNature']
    PveWater = request.json["partyId"] if request.json["type"] == "PveWater" else profile_query['profileChanges'][0]['profile']['stats']['attributes']['default_parties']['PveWater']
    return sanic.response.json({
        "profileRevision": int(request.args.get("rvn")) + 1,
        "profileId": "profile0",
        "profileChangesBaseRevision": int(request.args.get("rvn")),
        "profileChanges": [
            {
                "changeType": "statModified",
                "name": "default_parties",
                "value": {
                    "PveLight": PveLight,
                    "LastPvePartyUsed": request.json["partyId"],
                    "PveFire": PveFire,
                    "PveDark": PveDark,
                    "PveNature": PveNature,
                    "PveWater": PveWater
                }
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
