"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the price engine for calculating tax
"""
import sanic
from .price import price
from .version import pe_version

priceengine = sanic.Blueprint.group(price, pe_version, url_prefix="/priceengine")
