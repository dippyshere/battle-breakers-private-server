"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the purchase page with the epic games purchase flow
"""
import sanic
from .purchaseflow import purchase_flow

purchase = sanic.Blueprint.group(purchase_flow)
