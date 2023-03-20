"""
Handles the silly 3rd party trackers
app.adjust.com seen in 1.0, 1.1, 1.2
"""

import sanic

adjust = sanic.Blueprint("adjust")


# undocumented
@adjust.route("/session", methods=["POST"])
async def adjust_session(request):
    """
    Handles the stupid tracker in older versions
    :param request: The request object
    :return: The response object (200)
    """
    return sanic.response.json({})


# undocumented
@adjust.route("/event", methods=["POST"])
async def adjust_event(request):
    """
    Handles the stupid tracker in older versions
    :param request: The request object
    :return: The response object (200)
    """
    return sanic.response.json({})


# undocumented
@adjust.route("/attribution", methods=["GET"])
async def attribution(request):
    """
    Handles the stupid tracker in older versions
    :param request: The request object
    :return: The response object (200)
    """
    return sanic.response.json({})
