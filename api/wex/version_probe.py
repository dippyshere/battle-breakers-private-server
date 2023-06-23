"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the mcp version probe
"""

import sanic

from utils.sanic_gzip import Compress

compress = Compress()
wex_version_probe = sanic.Blueprint("wex_version_probe")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/game/version-probe.md
@wex_version_probe.route("/api/game/version-probe", methods=['GET'])
@compress.compress()
async def version_probe(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    Handles the version probe request
    :param request: The request object
    :return: The response object
    """
    # Version probe can call upon different actions for the client to take
    # The client supports the commands: launch_url:<url>, stop_url:<url>, switch_env:<mcpenv>
    # launch_url will open the url in the client's default browser, and continue the login process
    # stop_url will open the url in the client's default browser, and halt the login process
    # switch_env will switch the client to the specified MCP environment (live, devtesting, etc),
    # the client will then call the version probe again after switching
    return sanic.response.text("")
