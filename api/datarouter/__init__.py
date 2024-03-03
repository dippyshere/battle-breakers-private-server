"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the telemetry data from the client
"""
import sanic
from .data import data
from .version import datarouter_version

datarouter = sanic.Blueprint.group(data, datarouter_version, url_prefix="/datarouter")
