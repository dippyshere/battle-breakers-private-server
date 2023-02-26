"""
Handles the tax calculation
"""

import sanic
import orjson

wex_timeline = sanic.Blueprint("wex_timeline")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/calendar/v1/timeline.md
@wex_timeline.route("/wex/api/calendar/v1/timeline", methods=["GET"])
async def calendar(request):
    """
    get calendar timeline
    :param request: The request object
    :return: The response object
    """
    with open("res/wex/api/calendar/v1/timeline.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))
