"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the bulk offers for wex catalog
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
bulk = sanic.Blueprint("catalog_bulk")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/catalog-public-service-prod.ol.epicgames.com/catalog/api/shared/bulk/offers.md
@bulk.route("/api/shared/bulk/offers", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def offers(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Get offers
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json(await request.app.ctx.read_file(f"res/catalog/api/shared/bulk/offers.json"))
