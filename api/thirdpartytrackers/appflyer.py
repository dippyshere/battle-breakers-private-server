"""
Handles the silly 3rd party trackers
appflyer seen in 1.71
"""

import sanic

appflyer = sanic.Blueprint("appflyer")


# undocumented
@appflyer.route("/api/v4/androidevent", methods=["POST"])
async def appflyer_event(request):
    """
    Handles the stupid tracker in older versions
    :param request: The request object
    :return: The response object (200)
    """
    return sanic.response.json({})
