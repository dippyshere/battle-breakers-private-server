"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the presence api
"""
import sanic
from .lastonline import lastonline
from .version import presence_version

presence = sanic.Blueprint.group(lastonline, presence_version, url_prefix="/presence")
