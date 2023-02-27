"""
Handles the log uploader
"""

import sanic

wex_log = sanic.Blueprint("wex_log_upload")


# undocumented
@wex_log.route("/wex/api/feedback/log-upload/<file>", methods=["POST"])
async def logupload(request, file):
    """
    Handles the log upload request
    :param request: The request object
    :param file: The file name
    :return: The response object (204)
    """
    return sanic.response.empty()
