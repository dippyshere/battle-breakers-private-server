"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the events timeline
"""

import sanic
import datetime

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
wex_timeline = sanic.Blueprint("wex_timeline")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/calendar/v1/timeline.md
@wex_timeline.route("/api/calendar/v1/timeline", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def calendar(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    get calendar timeline
    :param request: The request object
    :return: The response object
    """
    # with open("res/wex/api/calendar/v1/timeline.json", "r", encoding='utf-8') as file:
    #     return sanic.response.json(orjson.loads(file.read()))
    # return await sanic.response.file_stream("res/wex/api/calendar/v1/timeline.json", mime_type="application/json")
    timeline = await request.app.ctx.read_file("res/wex/api/calendar/v1/timeline.json")
    timeline["currentTime"] = await request.app.ctx.format_time()
    for channel in timeline["channels"]:
        for state in timeline["channels"][channel]["states"]:
            state["validFrom"] = await request.app.ctx.format_time((datetime.datetime.utcnow() - datetime.timedelta(hours=1)))
        timeline["channels"][channel]["cacheExpire"] = await request.app.ctx.format_time((datetime.datetime.utcnow() + datetime.timedelta(hours=2)))
    return sanic.response.json(timeline)
