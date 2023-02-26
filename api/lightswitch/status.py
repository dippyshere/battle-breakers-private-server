"""
Handles the service status for Battle Breakers
"""

import sanic

status = sanic.Blueprint("lightswitch_status")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/lightswitch-public-service-prod.ol.epicgames.com/lightswitch/api/service/bulk/status.md
@status.route("/lightswitch/api/service/bulk/status", methods=["GET"])
async def lightswitch(request):
    """
    Handles the lightswitch status request
    :param request: The request object
    :return: The response object
    """
    service_id = request.args.get("serviceId")
    return sanic.response.json([{
        "serviceInstanceId": service_id.lower(),
        "status": "UP",
        "message": "Battle Breakers is back :D",
        "maintenanceUri": None,
        "overrideCatalogIds": ["ae402a2cb61b4c5fa199ce5311cca724"],
        "allowedActions": ["PLAY", "DOWNLOAD"],
        "banned": False,
        "launcherInfoDTO": {
            "appName": service_id,
            "catalogItemId": "a53e821fbdc24181877243a8dbb63463",
            "namespace": "wex"
        }
    }])
