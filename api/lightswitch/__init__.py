"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the service status for Battle Breakers
"""
import sanic
from .status import status
from .version import lightswitch_version

lightswitch = sanic.Blueprint.group(status, lightswitch_version, url_prefix="/lightswitch")
