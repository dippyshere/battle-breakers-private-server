"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles miscellaneous endpoints
"""
import sanic
from .favicon import favicon
from .robots import robots
from .version import version

misc = sanic.Blueprint.group(favicon, robots, version)
