"""
Handles the mcp version probe
"""

import sanic

wex_version_probe = sanic.Blueprint("wex_version_probe")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/version-probe.md
@wex_version_probe.route("/wex/api/game/version-probe", methods=['GET'])
async def version_probe(request):
    """
    Handles the version probe request
    :param request: The request object
    :return: The response object
    """
    headers = {
        "X-EpicGames-McpVersion": "prod Release-1.88-1.88 build 107 cl 19310354",
        "X-EpicGames-ContentVersion": "1.88.244-r17036752",
        "X-EpicGames-MinBuild": "17036752"
    }
    return sanic.response.text("", headers=headers)
