"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the silly 3rd party trackers
"""
import sanic
from .adjust import adjust
from .appflyer import appflyer
from .helpshift import helpshift
from .ios import iosevent

trackers = sanic.Blueprint.group(adjust, appflyer, helpshift, iosevent)
