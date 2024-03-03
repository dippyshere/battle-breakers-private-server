"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the purchase page with the epic games purchase flow
"""
import sanic
from .purchaseflow import purchase_flow

purchase = sanic.Blueprint.group(purchase_flow)
