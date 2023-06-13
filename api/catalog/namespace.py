"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the namespace offers for epic catalog
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
namespace = sanic.Blueprint("catalog_namespace")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/catalog-public-service-prod06.ol.epicgames.com/catalog/api/shared/namespace/wex/bulk/items.md
@namespace.route("/api/shared/bulk/namespace/wex/bulk/items", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def items(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Get items
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json(await request.app.ctx.read_file(f"res/catalog/api/shared/namespace/wex/bulk/items.json"))
