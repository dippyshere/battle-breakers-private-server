"""
Handles the telemetry data from the client
"""

import sanic

data = sanic.Blueprint("datarouter_data")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/datarouter.ol.epicgames.com/datarouter/api/v1/public/data.md
@data.route("/datarouter/api/v1/public/data", methods=["POST"])
async def datarouter(request):
    """
    Handles the datarouter requests (telemetry)
    :param request: The request object
    :return: The response object (204)
    """
    return sanic.response.empty()
