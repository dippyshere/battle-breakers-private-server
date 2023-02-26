"""
Handles the tax calculation
"""

import sanic

wex_version_check = sanic.Blueprint("wex_version_check")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/v2/versioncheck/Windows.md
@wex_version_check.route("/wex/api/v2/versioncheck/Windows", methods=['GET'])
async def version_check_windows(request):
    """
    Handles the version check request
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({"type": "NO_UPDATE"})


@wex_version_check.route("/wex/api/v2/versioncheck/Android", methods=['GET'])
async def version_check_android(request):
    """
    Handles the version check request
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({"type": "NO_UPDATE"})
