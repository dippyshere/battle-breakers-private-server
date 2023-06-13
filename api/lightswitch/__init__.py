"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the service status for Battle Breakers
"""
import sanic
from .status import status
from .version import lightswitch_version

lightswitch = sanic.Blueprint.group(status, lightswitch_version, url_prefix="/lightswitch")
