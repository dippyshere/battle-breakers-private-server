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
    headers = {"Date": "Thu, 29 Dec 2022 06:07:55 GMT", "X-Epic-Device-ID": "68009daed09498667a8039cce09983ed", "X-Epic-Correlation-ID": "UE4-2f4c92e44a8a8420a867089329526852-F210356F48A4A08AF14720B3AE34B5B9-27A444314652A4B2519DBEA580BCAFE6"}
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
    }], headers=headers)
