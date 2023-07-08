"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Fetch domains that are compatible with epics single sign on system
"""

import sanic

from utils.sanic_gzip import Compress

compress = Compress()
ssodomains = sanic.Blueprint("account_ssodomains")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/Account%20Service/account/api/epicdomains/ssodomains.md
@ssodomains.route("/api/epicdomains/ssodomains", methods=["GET"])
@compress.compress()
async def epic_domains_sso_domains(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Get epic domains sso domains
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json(["unrealengine.com", "unrealtournament.com", "fortnite.com", "epicgames.com"])
