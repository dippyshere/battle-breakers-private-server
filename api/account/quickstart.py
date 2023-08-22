"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the quick start account creation
"""
import sanic

from utils.utils import authorized as auth, oauth_response, generate_eg1, uuid_generator, create_account, read_file, \
    token_generator, format_time, write_file

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
    new_account_id = await create_account()
    # make the new account headless, so the user can set a name
    account_info = await read_file(f"res/account/api/public/account/{new_account_id}.json")
    account_info["headless"] = True
    device_id = await uuid_generator()
    device_authorisation = {
        "deviceId": device_id,
        "accountId": new_account_id,
        "secret": (await token_generator()).upper(),
        "userAgent": request.headers.get("User-Agent"),
        "created": {
            "location": None,
            "ipAddress": request.ip,
            "dateTime": await format_time()
        }
    }
    account_info["extra"]["deviceAuths"].append(device_authorisation)
    await write_file(f"res/account/api/public/account/{new_account_id}.json", account_info)
    profile = await read_file(
        f"res/wex/api/game/v2/profile/{new_account_id}/QueryProfile/profile0.json")
    profile["stats"]["attributes"]["is_headless"] = True
    await write_file(
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
        "internalAuthKey": f"eg1~{await generate_eg1(sub=new_account_id, dn=None, clid=None, dvid=device_id)}",
        "deviceAuth": device_authorisation,
        "oauthSession": await oauth_response(sub=new_account_id, dvid=device_id)
    })
