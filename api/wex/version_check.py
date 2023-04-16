"""
Handles the version check
"""

import sanic

wex_version_check = sanic.Blueprint("wex_version_check")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/v2/versioncheck/Windows.md
@wex_version_check.route("/wex/api/v2/versioncheck/<platform>", methods=['GET'])
async def version_check(request, platform):
    """
    Handles the version check request
    :param request: The request object
    :param platform: The platform
    :return: The response object
    """
    return sanic.response.json({"type": "NO_UPDATE"})
