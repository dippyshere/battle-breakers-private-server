"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the sac code api
"""

import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
sac_code = sanic.Blueprint("sac_code")


# undocumented
@sac_code.route("/api/public/affiliates/slug/<sacSlug>", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def sac_code_info(request: sanic.request.Request, sacSlug: str) -> sanic.response.JSONResponse:
    """
    Get support a creator code info

    :param request: The request object
    :param sacSlug: The sac slug
    :return: The response object
    """
    search_dn = await request.app.ctx.get_account_id_from_display_name(sacSlug)
    if search_dn is not None:
        return sanic.response.json({
            "id": search_dn,
            "slug": sacSlug,
            "displayName": sacSlug,
            "status": "ACTIVE",
            "verified": True
        })
    raise sanic.exceptions.NotFound(sacSlug, context={
        "errorCode": "errors.com.epicgames.affiliate.slug_not_found",
        "errorMessage": "The creator code was not found.",
        "numericErrorCode": 16004
    })
