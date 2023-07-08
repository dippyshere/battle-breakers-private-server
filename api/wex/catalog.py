"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the store catalog
"""
import sanic

from utils.sanic_gzip import Compress
from utils.utils import authorized as auth

compress = Compress()
wex_catalog = sanic.Blueprint("wex_catalog")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/storefront/v2/catalog.md
@wex_catalog.route("/api/storefront/v2/catalog", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def wex_catalog_request(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    get store catalog
    :param request: The request object
    :return: The response object
    """
    catalog = await request.app.ctx.read_file("res/wex/api/storefront/v2/catalog.json")
    catalog["expiration"] = await request.app.ctx.format_time((await request.app.ctx.get_nearest_12_hour_interval()))
    # TODO: troubleshoot error in 1.3 and 1.4
    #  Attempted to access index 0 from array 'ItemGrants' of length 0 in '/Script/WorldExplorers.WExpStoreButton'
    # if request.headers.get("User-Agent") == "User-Agent: game=WorldExplorers, engine=UE4, build=1.3.130-r3604802":
    #     for store in catalog["storefronts"]:
    #         for entry in store["catalogEntries"]:
    #             if entry.get("itemGrants") is None or entry.get("itemGrants") == []:
    #                 entry["itemGrants"] = [
    #                     {
    #                         "templateId": "Ore:Ore_Magicite",
    #                         "quantity": 1
    #                     }
    #                 ]
    return sanic.response.json(catalog)
