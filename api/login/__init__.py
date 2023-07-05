"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account related requests
"""
import sanic
from .csrf import csrf_req
from .exchange import id_exchange
from .guided import guided_login
from .register import register_login
from .token import login_token

login = sanic.Blueprint.group(csrf_req, id_exchange, guided_login, register_login, login_token)
