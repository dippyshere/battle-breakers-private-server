"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the CSRF code generation
"""
import sanic

from utils.exceptions import errors

from utils.sanic_gzip import Compress

compress = Compress()
csrf_req = sanic.Blueprint("csrf_req")


# stub
@csrf_req.route("/id/api/csrf", methods=["POST"])
@compress.compress()
async def csrf_route(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Generates a CSRF code
    :param request: The request object
    :return: The response object
    """
    raise errors.com.epicgames.not_found()
    # return sanic.response.json({
    #     "token": re.sub(r"[^a-zA-Z0-9]", "", os.urandom(32).hex())
    # })
