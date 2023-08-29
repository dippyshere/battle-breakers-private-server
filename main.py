"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.
"""
from typing import Any

from api import api
from utils import utils, error_handler
from utils.profile_system import MCPProfile, MCPItem
import middleware.mcp_middleware

import orjson
import sanic
import sanic_ext
import colorama
import motor.motor_asyncio

try:
    import tomllib as toml
except ModuleNotFoundError:
    import tomli as toml

colorama.init()


def custom_serialise(obj: Any) -> dict[str, Any]:
    """
    Custom serialiser for orjson to handle the custom objects
    :param obj: The object to serialize
    :return: The serialisable object
    """
    if isinstance(obj, MCPProfile):
        return obj.profile
    if isinstance(obj, MCPItem):
        return obj.item
    # Handle other custom serialization logic here
    raise TypeError(f"Object of type '{obj.__class__.__name__}' is not JSON serializable")


app: sanic.app.Sanic = sanic.app.Sanic("dippy_breakers", dumps=lambda obj: orjson.dumps(obj, default=custom_serialise),
                                       loads=orjson.loads)
app.config.CORS_ORIGINS = "*"
app.config.CORS_ALWAYS_SEND = True
app.blueprint(api)
sanic_ext.Extend(app)

with open("utils/config.toml", "rb") as config_file:
    config: dict[str, Any] = toml.load(config_file)
    config_file.close()

app.ctx.public_key = utils.public_key
app.error_handler = error_handler.CustomErrorHandler()
app.register_middleware(middleware.mcp_middleware.add_mcp_headers, "response")
app.ctx.database = motor.motor_asyncio.AsyncIOMotorClient(config["database"]["uri"])[config["database"]["database"]]
app.ctx.accounts = {}
app.ctx.friends = {}
app.ctx.profiles = {}
app.ctx.invalid_tokens = []


@app.main_process_stop
async def main_stop(*_: Any) -> None:
    """
    Called when the server is stopped
    :param _: The loop
    """
    for profile in app.ctx.profiles.values():
        await profile.flush_changes()
        await profile.save_profile()
    for profile in app.ctx.friends.values():
        await profile.save_friends()


# fast=true
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, auto_reload=True, access_log=False)
