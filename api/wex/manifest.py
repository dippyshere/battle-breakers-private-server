"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the manifest
"""
import aiofiles
import sanic

from utils.sanic_gzip import Compress

compress = Compress()
wex_manifest = sanic.Blueprint("wex_manifest")


# undocumented
@wex_manifest.route("/api/game/v2/manifests/<manifest>", methods=['GET'])
@compress.compress()
async def wex_cloudv3_manifests(request: sanic.request.Request, manifest: str) -> sanic.response.HTTPResponse:
    """
    Handles the manifest request for builds before build manifest (i.e. v1.5 and older)
    :param request: The request object
    :param manifest: The manifest
    :return: The response object
    """
    # yes, this is more ugly than the regex in utils, however its roughly 2-8x faster
    try:
        changelist = request.headers.get("User-Agent").split('version=')[1].split(",")[0].split("-")[1].split("+")[0]
    except:
        changelist = None
    if changelist is None:
        changelist = "3891207"

    # ~ 2ms
    # try:
    #     with open(f"res/wex/api/game/v2/manifests/CL_{changelist}/{manifest}", "rb") as f:
    #         manifest = orjson.dumps(orjson.loads(f.read())).decode("utf-8")
    # except:
    #     raise sanic.exceptions.FileNotFound("Manifest not found")
    # return sanic.response.text(manifest, content_type="text/text")

    # ~ 150ms
    # try:
    #     return await sanic.response.file(f"res/wex/api/game/v2/manifests/CL_{changelist}/{manifest}",
    #                                      mime_type="text/plain")
    # except:
    #     raise sanic.exceptions.FileNotFound("Manifest not found")

    # ~ 1.5ms
    try:
        async with aiofiles.open(f"res/wex/api/game/v2/manifests/CL_{changelist}/{manifest}", "rb") as file:
            return sanic.response.raw(await file.read(), content_type="text/text")
    except:
        raise sanic.exceptions.FileNotFound("Manifest not found")
