"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the catalog endpoints
"""
import sanic
from .bulk import bulk
from .namespace import catalog_namespace
from .version import catalog_version

catalog = sanic.Blueprint.group(bulk, catalog_namespace, catalog_version, url_prefix="/catalog")
