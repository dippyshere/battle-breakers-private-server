"""
get single sign on domains idk
"""

import sanic

ssodomains = sanic.Blueprint("account_ssodomains")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/account-public-service-prod.ol.epicgames.com/account/api/epicdomains/ssodomains.md
@ssodomains.route("/account/api/epicdomains/ssodomains", methods=["GET"])
async def epic_domains_sso_domains(request):
    """
    Get epic domains sso domains
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json(["unrealengine.com", "unrealtournament.com", "fortnite.com", "epicgames.com"])
