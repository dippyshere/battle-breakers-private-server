"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the presence api
"""
import sanic
from .lastonline import lastonline
from .version import presence_version

presence = sanic.Blueprint.group(lastonline, presence_version, url_prefix="/presence")
