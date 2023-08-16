"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the keychain stub
"""
import sanic

from utils.sanic_gzip import Compress
from utils.utils import authorized as auth

compress = Compress()
wex_keychain = sanic.Blueprint("wex_keychain")


# https://github.com/LeleDerGrasshalmi/FortniteEndpointsDocumentation/blob/main/EpicGames/WexService/Game/Catalog/Keychain.md
@wex_keychain.route("/api/storefront/v2/keychain", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def wex_catalog_request(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Get the keychain for encrypted dynamic paks. The game never featured any pak encryption (dynamic or not), so this
    is likely a stub incase they ever wanted to add it and could make it work with their dynamic pak system.
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json([])
