"""
Handles the manifest cdn downloads
"""

import sanic

manifest = sanic.Blueprint("cdn_manifest")


# undocumented
@manifest.route("/<version>", methods=["GET"])
async def manifest_req(request, version):
    """
    Handles the manifest check
    :param request: The request object
    :param version: The version
    :return: The response object (204)
    """
    return sanic.response.empty()


# undocumented
@manifest.route("/<version>/<file>", methods=["GET"])
async def build_manifest(request, version, file):
    """
    Handles the build manifest files
    :param request: The request object
    :param version: The version
    :param file: The file
    :return: The response object (204)
    """
    return sanic.response.text(f"""$BUILD_ID = {version}
$NUM_ENTRIES = 1
pakchunk1_pak1.pak	1223	SHA1:43e5fc94189a7bfc19b23e410b062fcdf0868333	1	Windows/pakchunk1_pak1.pak
""")


# undocumented
@manifest.route("/<version>/<file>/<pakchunk>", methods=["GET"])
async def manifest_pak(request, version, file, pakchunk):
    """
    Handles the pak chunk downloads
    :param request: The request object
    :param version: The version
    :param file: The file
    :param pakchunk: The pakchunk
    :return: The response object (204)
    """
    return sanic.response.empty()
