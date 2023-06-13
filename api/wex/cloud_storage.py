"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the cloud storage systems
"""
import datetime
import hashlib
import os

import sanic

from utils.sanic_gzip import Compress
from utils.utils import authorized as auth

compress = Compress()
wex_cloud = sanic.Blueprint("wex_cloud")


# https://github.com/dippyshere/battle-breakers-documentation/blob/main/docs/wex-public-service-live-prod.ol.epicgames.com/wex/api/storefront/v2/catalog.md
@wex_cloud.route("/api/cloudstorage/system", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def cloudstorage_system(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Handles the cloudstorage system request
    :param request: The request object
    :return: The response object
    """
    files = []
    for file in os.listdir("res/wex/api/cloudstorage/system"):
        with open(f"res/wex/api/cloudstorage/system/{file}", "rb") as f:
            data = f.read()
        # best solution tbh
        if file == "DefaultEngine.ini":
            unique_filename = "a6b5e5b09d0b426db3616c919b2af9b0"
        elif file == "DefaultGame.ini":
            unique_filename = "b91b0a42b48740bfaaf0acae1df48cb1"
        else:
            unique_filename = file
        files.append({
            "uniqueFilename": unique_filename,
            "filename": file,
            "hash": hashlib.sha1(data).hexdigest(),
            "hash256": hashlib.sha256(data).hexdigest(),
            "length": len(data),
            "contentType": "application/octet-stream",
            "uploaded": datetime.datetime.fromtimestamp(
                os.path.getmtime(f"res/wex/api/cloudstorage/system/{file}")).isoformat() + "Z",
            "storageType": "S3",  # Totally, I'm made of money and can afford to host this on S3
            "doNotCache": False
        })
    return sanic.response.json(files)


@wex_cloud.route("/api/cloudstorage/system/config", methods=["GET"])
@auth(allow_basic=True)
@compress.compress()
async def cloudstorage_system_config(request: sanic.request.Request) -> sanic.response.JSONResponse:
    """
    Handles the cloudstorage system configuration request
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "lastUpdated": await request.app.ctx.format_time(os.path.getmtime("api/wex/cloud_storage.py")),
        "disableV2": False,
        "isAuthenticated": True,
        "enumerateFilesPath": "/api/cloudstorage/system",
        "enableMigration": False,
        "enableWrites": False,
        "epicAppName": "Live",
        "transports": {
            "McpProxyTransport": {
                "name": "McpProxyTransport",
                "type": "ProxyStreamingFile",
                "appName": "worldexplorers",
                "isEnabled": False,
                "isRequired": True,
                "isPrimary": True,
                "timeoutSeconds": 30,
                "priority": 10
            },
            "McpSignatoryTransport": {
                "name": "McpSignatoryTransport",
                "type": "ProxySignatory",
                "appName": "worldexplorers",
                "isEnabled": False,
                "isRequired": False,
                "isPrimary": False,
                "timeoutSeconds": 30,
                "priority": 20
            },
            "DssDirectTransport": {
                "name": "DssDirectTransport",
                "type": "DirectDss",
                "appName": "worldexplorers",
                "isEnabled": True,
                "isRequired": False,
                "isPrimary": False,
                "timeoutSeconds": 30,
                "priority": 30
            }
        }
    })


@wex_cloud.route("/api/cloudstorage/system/<filename>", methods=['GET'])
@auth(allow_basic=True)
async def cloudstorage_system_get_file(request: sanic.request.Request, filename: str) -> sanic.response.HTTPResponse:
    """
    Handles the cloudstorage system get request
    :param request: The request object
    :param filename: The filename
    :return: The response object
    """
    if filename == "a6b5e5b09d0b426db3616c919b2af9b0":
        filename = "DefaultEngine.ini"
    elif filename == "b91b0a42b48740bfaaf0acae1df48cb1":
        filename = "DefaultGame.ini"
    if not os.path.exists(f"res/wex/api/cloudstorage/system/{filename}"):
        raise sanic.exceptions.FileNotFound(f"File {filename} not found")
    data = await request.app.ctx.read_file(f"res/wex/api/cloudstorage/system/{filename}")
    return sanic.response.raw(data, content_type="application/octet-stream")


@wex_cloud.route("/api/cloudstorage/user/<accountId>", methods=['GET'])
@auth(strict=True)
async def cloudstorage_user(request: sanic.request.Request, accountId: str) -> sanic.response.JSONResponse:
    """
    Handles the cloudstorage user request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    files = []
    for file in os.listdir("res/wex/api/cloudstorage/user"):
        data = await request.app.ctx.read_file(f"res/wex/api/cloudstorage/user/{file}")
        files.append({
            "uniqueFilename": file,
            "filename": file,
            "hash": hashlib.sha1(data).hexdigest(),
            "hash256": hashlib.sha256(data).hexdigest(),
            "length": len(data),
            "contentType": "application/octet-stream",
            "uploaded": datetime.datetime.fromtimestamp(
                os.path.getmtime(f"res/wex/api/cloudstorage/user/{file}")).isoformat() + "Z",
            "storageType": "S3",
            "doNotCache": False
        })
    return sanic.response.json(files)


@wex_cloud.route("/api/cloudstorage/user/<accountId>/<filename>", methods=['GET'])
@auth(strict=True)
async def cloudstorage_user_get_file(request: sanic.request.Request, accountId: str,
                                     filename: str) -> sanic.response.HTTPResponse:
    """
    Handles the cloudstorage user get request
    :param request: The request object
    :param accountId: The account id
    :param filename: The filename
    :return: The response object
    """
    if not os.path.exists(f"res/wex/api/cloudstorage/user/{filename}"):
        raise sanic.exceptions.FileNotFound(f"File {filename} not found")
    with open(f"res/wex/api/cloudstorage/user/{filename}", "rb") as f:
        data = f.read()
    return sanic.response.raw(data, content_type="application/octet-stream")


@wex_cloud.route("/api/cloudstorage/user/<accountId>/<filename>", methods=['PUT'])
@auth(strict=True)
async def cloudstorage_user_put_file(request: sanic.request.Request, accountId: str,
                                     filename: str) -> sanic.response.HTTPResponse:
    """
    Handles the cloudstorage user upload request
    :param request: The request object
    :param accountId: The account id
    :param filename: The filename
    :return: The response object
    """
    raise sanic.exceptions.SanicException("How about no", status_code=418)
