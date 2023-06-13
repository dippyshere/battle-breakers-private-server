"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the silly 3rd party trackers
"""
import sanic
from .adjust import adjust
from .appflyer import appflyer

trackers = sanic.Blueprint.group(adjust, appflyer)
