"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the events timeline
"""

import sanic

from utils import types
from utils.utils import authorized as auth, format_time

from utils.sanic_gzip import Compress

compress = Compress()
wex_timeline = sanic.Blueprint("wex_timeline")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/World%20Explorers%20Service/wex/api/calendar/v1/timeline.md
@wex_timeline.route("/api/calendar/v1/timeline", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def calendar(request: types.BBRequest) -> sanic.response.JSONResponse:
    """
    get calendar timeline
    :param request: The request object
    :return: The response object
    """
    # valid_from = await format_time(
    #     (datetime.datetime.utcnow() - datetime.timedelta(hours=1)))
    # cache_expire = await format_time(
    #     (datetime.datetime.utcnow() + datetime.timedelta(hours=2)))
    # timeline = await read_file("res/wex/api/calendar/v1/timeline.json")
    # for channel in timeline["channels"]:
    #     for state in timeline["channels"][channel]["states"]:
    #         state["validFrom"] = await format_time((datetime.datetime.utcnow() - datetime.timedelta(hours=1)))
    #     timeline["channels"][channel]["cacheExpire"] = await format_time(
    #         (datetime.datetime.utcnow() + datetime.timedelta(hours=2)))
    # return sanic.response.json(timeline)
    return sanic.response.json({
        "channels": await request.app.ctx.calendar.update_required_events(),
        "eventsTimeOffsetHrs": 0.0,
        "cacheIntervalMins": 15.0,
        "currentTime": await format_time()
    })
