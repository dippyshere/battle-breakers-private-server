"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the service status for Battle Breakers
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
status = sanic.Blueprint("lightswitch_status")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/Lightswitch%20Service/lightswitch/api/service/bulk/status.md
@status.route("/api/service/bulk/status", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def lightswitch_bulk(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Handles the lightswitch bulk status request
    :param request: The request object
    :return: The response object
    """
    service_id = request.args.getlist("serviceId")
    services = []
    if not service_id:
        service_id = ["WorldExplorersLive"]
    for service in service_id:
        services.append({
            "serviceInstanceId": service.lower(),
            "status": "UP",  # "UP" for online, "DOWN" for maintenance, "RESTRICTED" for partial access
            "message": "Battle Breakers is back :D",
            "maintenanceUri": None,
            "overrideCatalogIds": ["ae402a2cb61b4c5fa199ce5311cca724"],
            "allowedActions": ["PLAY", "DOWNLOAD"],
            "banned": False,
            "launcherInfoDTO": {
                "appName": service,
                # not bothered / required to fix this for other services
                "catalogItemId": "a53e821fbdc24181877243a8dbb63463",
                "namespace": "wex"
            },
            "timeToShutdownInMs": -1
        })
    return sanic.response.json(services)


# undocumented
@status.route("/api/service/<serviceId>/status", methods=["GET"])
@compress.compress()
async def lightswitch_service(request: sanic.request.Request, serviceId: str) -> sanic.response.JSONResponse:
    """
    Handles the lightswitch status request
    :param request: The request object
    :param serviceId: The service id
    :return: The response object
    """
    return sanic.response.json([{
        "serviceInstanceId": serviceId.lower(),
        "status": "UP",  # "UP" for online, "DOWN" for maintenance, "RESTRICTED" for partial access
        "message": "Battle Breakers is back :D",
        "maintenanceUri": None,
        "overrideCatalogIds": ["ae402a2cb61b4c5fa199ce5311cca724"],
        "allowedActions": ["PLAY", "DOWNLOAD"],
        "banned": False,
        "launcherInfoDTO": {
            "appName": serviceId,
            "catalogItemId": "a53e821fbdc24181877243a8dbb63463",
            "namespace": "wex"
        },
        "timeToShutdownInMs": -1
    }])
