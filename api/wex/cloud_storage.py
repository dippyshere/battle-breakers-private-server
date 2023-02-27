"""
Handles the cloud storage systems
"""

import sanic

wex_cloud = sanic.Blueprint("wex_cloud")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/storefront/v2/catalog.md
@wex_cloud.route("/wex/api/cloudstorage/system", methods=["GET"])
async def cloudstorage_system(request):
    """
    Handles the cloudstorage system request
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json([{
        "uniqueFilename": "a6b5e5b09d0b426db3616c919b2af9b0",
        "filename": "DefaultEngine.ini",
        "hash": "ac740e157b4ef5c578e76f50ee8997ffb5c9f442",
        "hash256": "ab74b8b51e673b3fa8095192e6463de35e6683fcaacf38538bd0392f6e6b9894",
        "length": 137,
        "contentType": "application/octet-stream",
        "uploaded": "2019-12-15T19:36:11.935Z",
        "storageType": "S3",
        "doNotCache": False
    }, {
        "uniqueFilename": "b91b0a42b48740bfaaf0acae1df48cb1",
        "filename": "DefaultGame.ini",
        "hash": "3e985d66a070a1c9b9aab16a7210c81a7f6b6754",
        "hash256": "6037e7333f5dbf974e2b24148232f52d594a99b1db402f4a9af485f7b8e46527",
        "length": 1004,
        "contentType": "application/octet-stream",
        "uploaded": "2019-11-19T02:12:44.627Z",
        "storageType": "S3",
        "doNotCache": False
    }])


@wex_cloud.route("/wex/api/cloudstorage/system/DefaultGame.ini", methods=['GET'])
async def cloudstorage_system_default_game(request):
    """
    Handles the cloudstorage system default game request
    :param request: The request object
    :return: The response object
    """
    with open("res/wex/api/cloudstorage/system/DefaultGame.ini", "r", encoding='utf-8') as f:
        default_game = f.read()
    return sanic.response.raw(default_game)


@wex_cloud.route("/wex/api/cloudstorage/system/DefaultEngine.ini", methods=['GET'])
async def cloudstorage_system_default_engine(request):
    """
    Handles the cloudstorage system default engine request
    :param request: The request object
    :return: The response object
    """
    with open("res/wex/api/cloudstorage/system/DefaultEngine.ini", "r", encoding='utf-8') as f:
        default_engine = f.read()
    return sanic.response.raw(default_engine)
