"""
Handles profile queries
"""

import sanic

wex_profile_send_gift = sanic.Blueprint("wex_profile_send_gift")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/QueryProfile(profile0).md
@wex_profile_send_gift.route("/wex/api/game/v2/profile/<accountId>/SendGiftPoints", methods=["POST"])
async def send_gift_points(request, accountId: str):
    """
    Handles the send gift point request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json({
        "profileRevision": 39840,
        "profileId": "profile0",
        "profileChangesBaseRevision": 39838,
        "profileChanges": [{
            "changeType": "statModified",
            "name": "activity",
            "value": {
                "a": {
                    "date": "2022-12-28T00:00:00.000Z",
                    "claimed": False,
                    "props": {
                        "BaseBonus": 10
                    }
                },
                "b": {
                    "date": "2022-12-27T00:00:00.000Z",
                    "claimed": True,
                    "props": {
                        "BaseBonus": 10,
                        "EnergySpent": 3
                    }
                },
                "standardGift": 10
            }
        }],
        "profileCommandRevision": 23699,
        "serverTime": "2022-12-28T11:37:06.741Z",
        "multiUpdate": [{
            "profileRevision": 9864,
            "profileId": "friends",
            "profileChangesBaseRevision": 9862,
            "profileChanges": [],
            "profileCommandRevision": 8247
        }],
        "responseVersion": 1
    })
