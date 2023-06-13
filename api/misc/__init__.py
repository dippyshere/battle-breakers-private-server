"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles miscellaneous endpoints
"""
import sanic
from .favicon import favicon
from .version import version

misc = sanic.Blueprint.group(favicon, version)
