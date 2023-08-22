"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the log uploader
"""
import sanic

from utils.utils import authorized as auth, write_file

from utils.sanic_gzip import Compress

compress = Compress()
wex_log = sanic.Blueprint("wex_log_upload")


# undocumented
@wex_log.route("/api/feedback/log-upload/<file>", methods=["POST", "PUT"])
@auth(allow_basic=True)
@compress.compress()
async def logupload(request: sanic.request.Request, file: str) -> sanic.response.HTTPResponse:
    """
    Handles the log upload request
    :param request: The request object
    :param file: The file name
    :return: The response object (204)
    """
    if int(request.headers.get("Content-Length")) > 5242880:
        raise sanic.exceptions.PayloadTooLarge("File is too large, I'm not a free s3 bucket >_<")
    await write_file(f"res/wex/api/feedback/log-upload/{file}", request.body, False)
    return sanic.response.empty()
