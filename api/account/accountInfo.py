"""
Handles the account endpoint
"""

import sanic
import orjson

account_info = sanic.Blueprint("account_info")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e21.md
@account_info.route("/account/api/public/account/<accountid>", methods=["GET"])
async def account(request, accountid):
    """
    Get account info
    :param request: The request object
    :param accountid: The account id
    :return: The response object
    """
    with open("res/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e21/account.json", "r",
              encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
