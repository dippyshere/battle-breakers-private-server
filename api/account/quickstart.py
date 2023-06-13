"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the quick start account creation
"""
import sanic

from utils.utils import authorized as auth

from utils.sanic_gzip import Compress

compress = Compress()
account_quickstart = sanic.Blueprint("account_quickstart")


# undocumented
@account_quickstart.route("/api/public/account", methods=["POST"])
@auth(allow_basic=True)
@compress.compress()
async def quickstart(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """
    Create a quick start account

    :param request: The request object
    :return: The response object
    """
    new_account_id = await request.app.ctx.create_account()
    # make the new account headless, so the user can set a name
    account_info = await request.app.ctx.read_file(f"res/account/api/public/account/{new_account_id}.json")
    account_info["headless"] = True
    device_authorisation = {
        "deviceId": await request.app.ctx.token_generator(),
        "accountId": new_account_id,
        "secret": (await request.app.ctx.token_generator()).upper(),
        "userAgent": request.headers.get("User-Agent"),
        "created": {
            "location": None,
            "ipAddress": request.ip,
            "dateTime": await request.app.ctx.format_time()
        }
    }
    account_info["extra"]["deviceAuths"].append(device_authorisation)
    await request.app.ctx.write_file(f"res/account/api/public/account/{new_account_id}.json", account_info)
    profile = await request.app.ctx.read_file(
        f"res/wex/api/game/v2/profile/{new_account_id}/QueryProfile/profile0.json")
    profile["stats"]["attributes"]["is_headless"] = True
    await request.app.ctx.write_file(
        f"res/wex/api/game/v2/profile/{new_account_id}/QueryProfile/profile0.json", profile)
    return sanic.response.json({
        "accountInfo": {
            "id": new_account_id,
            "failedLoginAttempts": 0,
            "numberOfDisplayNameChanges": 0,
            "ageGroup": "ADULT",
            "headless": True,
            "country": "AU",
            "preferredLanguage": "en",
            "canUpdateDisplayName": True,
            "tfaEnabled": False,
            "emailVerified": False,
            "minorVerified": False,
            "minorExpected": False,
            "minorStatus": "NOT_MINOR",
            "cabinedMode": False,
            "hasHashedEmail": False
        },
        "internalAuthKey": f"eg1~{await request.app.ctx.generate_eg1(sub=new_account_id, dn=None, clid=None, dvid=None)}",
        "deviceAuth": device_authorisation,
        "oauthSession": await request.app.ctx.oauth_response(sub=new_account_id)
    })
