"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the entitlement check for the launcher
"""
import sanic
from .entitlement import entitlement
from .version import entitlement_version

entitlements = sanic.Blueprint.group(entitlement, entitlement_version, url_prefix="/entitlement")
