"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.
"""
from typing import Any

from api import api
from utils import utils, error_handler
from utils.profile_system import McpProfile
import middleware.mcp_middleware

import orjson
import sanic
import sanic_ext
import colorama


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
    if isinstance(obj, McpProfile):
        return obj.profile
    # Handle other custom serialization logic here
    raise TypeError(f"Object of type '{obj.__class__.__name__}' is not JSON serializable")


app = sanic.app.Sanic("dippy_breakers", dumps=lambda obj: orjson.dumps(obj, default=custom_serialise),
                      loads=orjson.loads)
app.config.CORS_ORIGINS = "*"
app.config.CORS_ALWAYS_SEND = True
app.blueprint(api)
sanic_ext.Extend(app)

with open("utils/config.toml", "rb") as config_file:
    config = toml.load(config_file)
    config_file.close()

app.ctx.read_file = utils.read_file
app.ctx.write_file = utils.write_file
app.ctx.get_nearest_12_hour_interval = utils.get_nearest_12_hour_interval
app.ctx.get_current_12_hour_interval = utils.get_current_12_hour_interval
app.ctx.format_time = utils.format_time
app.ctx.private_key = utils.private_key
app.ctx.public_key = utils.public_key
app.ctx.token_generator = utils.token_generator
app.ctx.generate_eg1 = utils.generate_eg1
app.ctx.generate_client_eg1 = utils.generate_client_eg1
app.ctx.generate_refresh_eg1 = utils.generate_refresh_eg1
app.ctx.generate_authorisation_eg1 = utils.generate_authorisation_eg1
app.ctx.parse_eg1 = utils.parse_eg1
app.ctx.to_insecure_hash = utils.to_insecure_hash
app.ctx.get_account_id_from_display_name = utils.get_account_id_from_display_name
app.ctx.get_account_id_from_email = utils.get_account_id_from_email
app.ctx.check_if_display_name_exists = utils.check_if_display_name_exists
app.ctx.oauth_response = utils.oauth_response
app.ctx.oauth_client_response = utils.oauth_client_response
app.ctx.create_account = utils.create_account
app.ctx.normalise_string = utils.normalise_string
app.ctx.load_datatable = utils.load_datatable
app.ctx.get_template_id_from_path = utils.get_template_id_from_path
app.ctx.extract_version_info = utils.extract_version_info
app.ctx.room_generator = utils.room_generator
app.error_handler = error_handler.CustomErrorHandler()
app.register_middleware(middleware.mcp_middleware.add_mcp_headers, "response")
app.ctx.accounts = {}
app.ctx.friends = {}
app.ctx.profiles = {}


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
