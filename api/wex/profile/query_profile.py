"""
Handles profile queries
"""

import sanic
import orjson

wex_profile_query = sanic.Blueprint("wex_profile_query")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/QueryProfile(profile0).md
@wex_profile_query.route("/wex/api/game/v2/profile/<accountId>/QueryProfile", methods=["POST"])
async def query_profile(request, accountId: str):
    """
    Handles the query profile request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    # with open(f"res/wex/api/game/v2/profile/{accountId}/QueryProfile/{request.args.get('profileId')}.json",
    #           "r", encoding='utf-8') as file:
    #     return sanic.response.json(orjson.loads(file.read()))
    with open(f"res/wex/api/game/v2/profile/smol/QueryProfile/{request.args.get('profileId')}.json",
              "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
