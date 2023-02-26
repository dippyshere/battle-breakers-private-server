"""
Handles the friends summary
"""

import sanic
import orjson

summary = sanic.Blueprint("friends_summary")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/friends-public-service-prod.ol.epicgames.com/friends/api/v1/ec0ebb7e56f6454e86c62299a7b32e21/summary.md
@summary.route("/friends/api/v1/<accountId>/summary", methods=["GET"])
async def friends_summary(request, accountId):
    """
    Get friends summary
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    try:
        with open(f"res/friends/api/v1/{accountId}/summary.json", "r", encoding='utf-8') as file:
            return sanic.response.json(orjson.loads(file.read()))
    except FileNotFoundError:
        return sanic.response.json({
            "friends": [],
            "incoming": [],
            "outgoing": [],
            "suggested": [],
            "blocklist": [
                {
                    "accountId": "85b9500e81b546fa9b0978b53d90675f"
                },
                {
                    "accountId": "a5f4958d844946538053d23ec063122a"
                },
                {
                    "accountId": "efb703bd474e4bdf85010e883313c78f"
                }
            ],
            "settings": {
                "acceptInvites": "public",
                "mutualPrivacy": "ALL"
            },
            "limitsReached": {
                "incoming": False,
                "outgoing": False,
                "accepted": False
            }
        })
