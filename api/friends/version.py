"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the silly version info
"""

import sanic

friends_version = sanic.Blueprint("friends_ver")


# undocumented
@friends_version.route("/api/version", methods=["GET"])
async def friends_version_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Version information

    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "app": "friends",
        "serverDate": await request.app.ctx.format_time(),
        "overridePropertiesVersion": "unknown",
        "cln": "34c899d2658aeae83527fa3dc6ec4d2ddafef3eb",
        "build": "b3133",
        "moduleName": "FriendsService-PublicService",
        "buildDate": "2023-05-04T12:23:47.360Z",
        "version": "2.3.242",
        "branch": "trunk",
        "modules": {
            "epic-xmpp-api-v1-base": {
                "cln": "5131a23c1470acbd9c94fae695ef7d899c1a41d6",
                "build": "b3595",
                "buildDate": "2019-07-30T09:11:06.587Z",
                "version": "0.0.1",
                "branch": "master"
            },
            "epic-common-core": {
                "cln": "ebb2a54d900d367b7770ad9402dd642f89c54fc0",
                "build": "b1226",
                "buildDate": "2023-04-19T11:42:25.969Z",
                "version": "5.1.3.20230419124130",
                "branch": "master"
            }
        }
    })
