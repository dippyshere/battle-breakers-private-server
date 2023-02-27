"""
Handles the public facing account info endpoint
"""

import sanic
import orjson

public_account = sanic.Blueprint("account_public")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/public/account.md
@public_account.route("/account/api/public/account", methods=["GET"])
async def public_account_info(request):
    """
    Get account info
    :param request: The request object
    :return: The response object
    """
    accountId = request.args.get("accountId")
    with open("res/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e21.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))


@public_account.route("/account/api/public/account/displayName/<displayName>", methods=["GET"])
async def account_displayname(request, displayName):
    """
    Get an account by name
    :param request: The request object
    :param displayName: The display name
    :return: The response object
    """
    return sanic.response.text("")


@public_account.route("/account/api/public/account/email/<email>", methods=["GET"])
async def account_email(request, email):
    """
    Get account by email
    :param request: The request object
    :param email: The email
    :return: The response object
    """
    return sanic.response.text("")
