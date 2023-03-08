"""
Handles adding epic friend and fetching their wex specific data
"""

import sanic

wex_profile_add_epic_friend = sanic.Blueprint("wex_profile_add_epic_friend")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/AddEpicFriend.md
@wex_profile_add_epic_friend.route("/wex/api/game/v2/profile/<accountId>/AddEpicFriend", methods=["POST"])
async def add_epic_friend(request, accountId):
    """
    This endpoint is used to fetch a new friend's wex data
    :param request: The request object
    :param accountId: The account id
    :return: The response object (204)
    """
    # TODO: Add Epic Friend
    return sanic.response.empty(status=200)
