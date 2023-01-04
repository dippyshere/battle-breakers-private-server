"""
A Battle Breakers Private server written in Python by Dippyshere
https://github.com/Dippyshere/Battle-Breakers-Private-Server
"""
import datetime

import orjson
import random
import string

import sanic
import colorama

try:
    import tomllib as toml
except ModuleNotFoundError:
    import tomli as toml

colorama.init()

app = sanic.app.Sanic('dippy_breakers', dumps=orjson.dumps, loads=orjson.loads)

with open("config.toml", "rb") as config_file:
    config = toml.load(config_file)
    config_file.close()


def token_generator(size=32, chars=string.hexdigits):
    """
    Generates a random string of characters
    :param size: The length of the token to generate
    :param chars: The characters to use
    :return: The generated string
    """
    return ''.join(random.choice(chars).lower() for _ in range(size))


# https://lightswitch-public-service-prod.ol.epicgames.com/lightswitch/api/service/bulk/status?serviceId=WorldExplorersLive
@app.route("/lightswitch/api/service/bulk/status", methods=["GET"])
async def lightswitch(request):
    """
    Handles the lightswitch status request
    :param request: The request object
    :return: The response object
    """
    serviceId = request.args.get("serviceId")
    return sanic.response.json([{
        "serviceInstanceId": serviceId.lower(),
        "status": "UP",
        "message": "This is a default status.",
        "maintenanceUri": None,
        "overrideCatalogIds": ["ae402a2cb61b4c5fa199ce5311cca724"],  # This is probably the MTX stuff
        "allowedActions": ["PLAY", "DOWNLOAD"],
        "banned": False,
        "launcherInfoDTO": {
            "appName": serviceId,
            "catalogItemId": "a53e821fbdc24181877243a8dbb63463",
            "namespace": "wex"
        }
    }])


# https://datarouter.ol.epicgames.com/datarouter/api/v1/public/data?SessionID=&AppID=WEX.LIVE&AppVersion=1.88.244-r17036752&UserID=2f4c92e44a8a8420a867089329526852%7C%7C83e93ca4-71a9-4951-bdcc-fb1730ad7313%7C68009daed09498667a8039cce09983ec%7C&AppEnvironment=datacollector-binary&UploadType=eteventstream
@app.route("/datarouter/api/v1/public/data", methods=["POST"])
async def datarouter(request):
    """
    Handles the datarouter requests (telemetry)
    :param request: The request object
    :return: The response object (204)
    """
    return sanic.response.empty()


# https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token
@app.route("/account/api/oauth/token", methods=["POST"])
async def oauth_token(request):
    """
    Handles the oauth token request
    :param request: The request object
    :return: The response object
    """
    if request.form.get('token_type') == 'eg1' and request.form.get('grant_type') == 'client_credentials':
        return sanic.response.json({
            "access_token": "eg1~eyJra0RkMyVUloRnBU.eyJhcHAiYmI3ZTU.hOmWdC7zo3u1mr62gONE7",
            "expires_in": 14400,
            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=14400)).strftime(
                "%Y-%m-%dT%H:%M:%S.000Z"),
            "token_type": "bearer",
            "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
            "internal_client": True,
            "client_service": "wex"
        })
    elif request.form.get('token_type') == 'eg1' and request.form.get('grant_type') == 'exchange_code':
        return sanic.response.json({
            "access_token": "eg1~eyJra0RkMyVUloRnBU.eyJhcHAiYmI3ZTU.hOmWdC7zo3u1mr62gONE7",
            "expires_in": 28800,
            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=28800)).strftime("%Y-%m-%dT%H:%M"
                                                                                                    ":%S.000Z"),
            "token_type": "bearer",
            "refresh_token": "eg1~eyJra0RkMyVUloRnBU.eyJhcHAiYmI3ZTU.hOmWdC7zo3u1mr62gONE7",
            "refresh_expires": 115200,
            "refresh_expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=115200)).strftime("%Y-%m"
                                                                                                             "-%dT%H"
                                                                                                             ":%M:%S"
                                                                                                             ".000Z"),
            "account_id": "ec0ebb7e56f6454e86c62299a7b32e21",
            "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
            "internal_client": True,
            "client_service": "wex",
            "displayName": "Dippyshere MbnM",
            "app": "wex",
            "in_app_id": "ec0ebb7e56f6454e86c62299a7b32e21",
            "device_id": "68009daed09498667a8039cce09983ec"
        })
    elif request.form.get('grant_type') == 'exchange_code':
        return sanic.response.json({
            "access_token": token_generator(),
            "expires_in": 28800,
            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=28800)).strftime("%Y-%m-%dT%H:%M"
                                                                                                    ":%S.000Z"),
            "token_type": "bearer",
            "refresh_token": token_generator(),
            "refresh_expires": 115200,
            "refresh_expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=115200)).strftime("%Y-%m"
                                                                                                             "-%dT%H"
                                                                                                             ":%M:%S"
                                                                                                             ".000Z"),
            "account_id": "ec0ebb7e56f6454e86c62299a7b32e21",
            "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
            "internal_client": True,
            "client_service": "wex",
            "displayName": "Dippyshere MbnM",
            "app": "wex",
            "in_app_id": "ec0ebb7e56f6454e86c62299a7b32e21",
            "device_id": "68009daed09498667a8039cce09983ec"
        })
    else:
        return sanic.response.json({
            "access_token": token_generator(),
            "expires_in": 14400,
            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=14400)).strftime(
                "%Y-%m-%dT%H:%M:%S.000Z"),
            "token_type": "bearer",
            "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
            "internal_client": True,
            "client_service": "wex"
        })


# https://account-public-service-prod.ol.epicgames.com/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e21/externalAuths
@app.route("/account/api/public/account/<accountid>/externalAuths", methods=["GET"])
async def external_auths(request, accountid):
    """
    Get external auths
    :param request: The request object
    :param accountid: The account id
    :return: The response object
    """
    return sanic.response.json([])


# https://account-public-service-prod.ol.epicgames.com/account/api/oauth/sessions/kill/eg1~
@app.route("/account/api/oauth/sessions/kill/", methods=["DELETE"])
async def kill_auth(request):
    """
    kill a token
    :param request: The request object
    :return: The response object
    """
    return sanic.response.empty()


# https://account-public-service-prod.ol.epicgames.com/account/api/oauth/verify?includePerms=true
@app.route("/account/api/oauth/verify", methods=["GET"])
async def verify_auth(request):
    """
    verify game auth
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({
        "token": "eg1~eyJra0RkMyVUloRnBU.eyJhcHAiYmI3ZTU.hOmWdC7zo3u1mr62gONE7",
        "session_id": "9bcccd0920424ce9b110b2e50bf05ce6",
        "token_type": "bearer",
        "client_id": "3cf78cd3b00b439a8755a878b160c7ad",
        "internal_client": True,
        "client_service": "wex",
        "account_id": "ec0ebb7e56f6454e86c62299a7b32e21",
        "expires_in": 28738,
        "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(seconds=28738)).strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"),
        "auth_method": "exchange_code",
        "display_name": "Dippyshere MbnM",
        "ext_auth_id": "1123",
        "ext_auth_type": "exchange_code",
        "ext_auth_method": "google_id_token",
        "ext_auth_display_name": "A",
        "app": "wex",
        "in_app_id": "ec0ebb7e56f6454e86c62299a7b32e21",
        "device_id": "68009daed09498667a8039cce09983ec",
        "perms": [{
            "resource": "blockList:ec0ebb7e56f6454e86c62299a7b32e21",
            "action": 14
        }, {
            "resource": "wexp:cloudstorage:system",
            "action": 2
        }, {
            "resource": "account:public:account:*",
            "action": 2
        }, {
            "resource": "account:oauth:exchangeTokenCode",
            "action": 15
        }, {
            "resource": "account:public:account",
            "action": 2
        }, {
            "resource": "priceengine:shared:offer:price",
            "action": 2
        }, {
            "resource": "xmpp:session:*:ec0ebb7e56f6454e86c62299a7b32e21",
            "action": 1
        }, {
            "resource": "wexp:wexp_role:client",
            "action": 15
        }, {
            "resource": "wexp:profile:ec0ebb7e56f6454e86c62299a7b32e21:*",
            "action": 15
        }, {
            "resource": "account:public:account:externalAuths",
            "action": 15
        }, {
            "resource": "wexp:calendar",
            "action": 2
        }, {
            "resource": "account:token:otherSessionsForAccountClient",
            "action": 8
        }, {
            "resource": "account:token:otherSessionsForAccountClientService",
            "action": 8
        }, {
            "resource": "account:public:account:deviceAuths",
            "action": 11
        }, {
            "resource": "wexp:cloudstorage:system:*",
            "action": 2
        }, {
            "resource": "serviceinstance",
            "action": 2
        }, {
            "resource": "wexp:storefront",
            "action": 2
        }, {
            "resource": "wexp:push:devices:ec0ebb7e56f6454e86c62299a7b32e21",
            "action": 15
        }, {
            "resource": "friends:ec0ebb7e56f6454e86c62299a7b32e21",
            "action": 15
        }]
    })


# https://account-public-service-prod.ol.epicgames.com/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e21
@app.route("/account/api/public/account/<accountid>", methods=["GET"])
async def account(request, accountid):
    """
    Get external auths
    :param request: The request object
    :param accountid: The account id
    :return: The response object
    """
    with open("res/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e21/account.json", "r",
              encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))


# https://account-public-service-prod.ol.epicgames.com/account/api/epicdomains/ssodomains
@app.route("/account/api/epicdomains/ssodomains", methods=["GET"])
async def epic_domains_sso_domains(request):
    """
    Get epic domains sso domains
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json(["unrealengine.com", "unrealtournament.com", "fortnite.com", "epicgames.com"])


# https://account-public-service-prod.ol.epicgames.com/account/api/public/account?accountId=ec0ebb7e56f6454e86c62299a7b32e21
@app.route("/account/api/public/account", methods=["GET"])
async def public_account_info(request):
    """
    Get account info
    :param request: The request object
    :return: The response object
    """
    accountId = request.args.get("accountId")
    with open("res/account/api/public/account/ec0ebb7e56f6454e86c62299a7b32e21.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))


# https://friends-public-service-prod.ol.epicgames.com/friends/api/v1/ec0ebb7e56f6454e86c62299a7b32e21/summary
@app.route("/friends/api/v1/<accountId>/summary", methods=["GET"])
async def friends_summary(request, accountId):
    """
    Get friends summary
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    with open("res/friends/api/v1/ec0ebb7e56f6454e86c62299a7b32e21/summary.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/entitlementCheck
@app.route("/wex/api/entitlementCheck", methods=["GET"])
async def entitlement_check(request):
    """
    This endpoint is used to check if the user has access to the game.
    :param request: The request object
    :return: The response object (204)
    """
    return sanic.response.empty()


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/storefront/v2/catalog
@app.route("/wex/api/storefront/v2/catalog", methods=["GET"])
async def catalog(request):
    """
    get calendar timeline
    :param request: The request object
    :return: The response object
    """
    with open("res/wex/api/storefront/v2/catalog.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/calendar/v1/timeline
@app.route("/wex/api/calendar/v1/timeline", methods=["GET"])
async def calendar(request):
    """
    get calendar timeline
    :param request: The request object
    :return: The response object
    """
    with open("res/wex/api/calendar/v1/timeline.json", "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/v2/versioncheck/Windows?version=1.88.244-r17036752-Windows
@app.route("/wex/api/v2/versioncheck/Windows", methods=['GET'])
async def version_check_windows(request):
    """
    Handles the version check request
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({"type": "NO_UPDATE"})


@app.route("/wex/api/v2/versioncheck/Android", methods=['GET'])
async def version_check_android(request):
    """
    Handles the version check request
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json({"type": "NO_UPDATE"})


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/version-probe
@app.route("/wex/api/game/version-probe", methods=['GET'])
async def version_probe(request):
    """
    Handles the version probe request
    :param request: The request object
    :return: The response object
    """
    headers = {
        "X-EpicGames-McpVersion": "prod Release-1.88-1.88 build 107 cl 19310354",
        "X-EpicGames-ContentVersion": "1.88.244-r17036752",
        "X-EpicGames-MinBuild": "17036752"
    }
    return sanic.response.text("", headers=headers)


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/cloudstorage/system
@app.route("/wex/api/cloudstorage/system", methods=["GET"])
async def cloudstorage_system(request):
    """
    Handles the cloudstorage system request
    :param request: The request object
    :return: The response object
    """
    return sanic.response.json([{
        "uniqueFilename": "a6b5e5b09d0b426db3616c919b2af9b0",
        "filename": "DefaultEngine.ini",
        "hash": "ac740e157b4ef5c578e76f50ee8997ffb5c9f442",
        "hash256": "ab74b8b51e673b3fa8095192e6463de35e6683fcaacf38538bd0392f6e6b9894",
        "length": 137,
        "contentType": "application/octet-stream",
        "uploaded": "2019-12-15T19:36:11.935Z",
        "storageType": "S3",
        "doNotCache": False
    }, {
        "uniqueFilename": "b91b0a42b48740bfaaf0acae1df48cb1",
        "filename": "DefaultGame.ini",
        "hash": "3e985d66a070a1c9b9aab16a7210c81a7f6b6754",
        "hash256": "6037e7333f5dbf974e2b24148232f52d594a99b1db402f4a9af485f7b8e46527",
        "length": 1004,
        "contentType": "application/octet-stream",
        "uploaded": "2019-11-19T02:12:44.627Z",
        "storageType": "S3",
        "doNotCache": False
    }])


@app.route("/wex/api/cloudstorage/system/DefaultGame.ini", methods=['GET'])
async def cloudstorage_system_default_game(request):
    """
    Handles the cloudstorage system default game request
    :param request: The request object
    :return: The response object
    """
    with open("res/wex/api/cloudstorage/system/DefaultGame.ini", "r", encoding='utf-8') as f:
        default_game = f.read()
    return sanic.response.raw(default_game)


@app.route("/wex/api/cloudstorage/system/DefaultEngine.ini", methods=['GET'])
async def cloudstorage_system_default_engine(request):
    """
    Handles the cloudstorage system default engine request
    :param request: The request object
    :return: The response object
    """
    with open("res/wex/api/cloudstorage/system/DefaultEngine.ini", "r", encoding='utf-8') as f:
        default_engine = f.read()
    return sanic.response.raw(default_engine)


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/QueryProfile?profileId=profile0&rvn=-1
@app.route("/wex/api/game/v2/profile/<accountId>/QueryProfile", methods=["POST"])
async def query_profile(request, accountId: str):
    """
    Handles the query profile request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    with open(f"res/wex/api/game/v2/profile/{accountId}/QueryProfile/{request.args.get('profileId')}.json",
              "r", encoding='utf-8') as file:
        return sanic.response.json(orjson.loads(file.read()))


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/ClaimLoginReward?profileId=profile0&rvn=9999
@app.route("/wex/api/game/v2/profile/<accountId>/ClaimLoginReward", methods=["POST"])
async def claim_login_reward(request, accountId: str):
    """
    Handles the daily reward request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json({
        "profileRevision": 40315,
        "profileId": "profile0",
        "profileChangesBaseRevision": 40314,
        "profileChanges": [{
            "changeType": "itemQuantityChanged",
            "itemId": "03e1d076-957e-43f2-9702-71d521413717",
            "quantity": 501
        }, {
            "changeType": "statModified",
            "name": "login_reward",
            "value": {
                "last_claim_time": "2022-12-29T05:43:30.806Z",
                "next_level": 187
            }
        }, {
            "changeType": "statModified",
            "name": "hammer_quest_energy",
            "value": {
                "energy_spent": 0,
                "energy_required": 100,
                "claim_count": 0
            }
        }, {
            "changeType": "statModified",
            "name": "activity",
            "value": {
                "a": {
                    "date": "2022-12-28T00:00:00.000Z",
                    "claimed": False,
                    "props": {
                        "HeroAcquired": 137,
                        "HeroPromote": 1,
                        "HeroEvolve": 1,
                        "MonsterPitLevelUp": 1,
                        "HeroFoil": 1,
                        "AccountLevelUp": 2,
                        "BaseBonus": 10,
                        "EnergySpent": 187
                    }
                },
                "b": {
                    "date": "2022-12-29T00:00:00.000Z",
                    "claimed": False,
                    "props": {
                        "BaseBonus": 10
                    }
                },
                "standardGift": 10
            }
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "f7c3b0c5-d208-4bc4-b6d5-054359784dd0",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "7b899484-837c-4eea-aa0d-a80ce97ae0d7",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "7585df88-2a1e-4ca4-b0ce-33ab0aaac483",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "88721a32-4602-46eb-9662-294610e2e7b5",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "ef81e090-a854-48fd-8924-ef7d07eb0301",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "b8ef336b-e07a-4c41-9b8c-5544746d55d6",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "9b0fffd3-92f3-4018-9799-0bd89c6804c3",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "b83d82de-0cd3-4eac-8cb5-9cfec3360853",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "8b1d13e5-6ee3-4265-96a8-c3e62646a87d",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "dff1fe19-d477-4249-8e2d-258c0df83c78",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "ab0cd5f2-2a8f-47df-8470-0de41c526669",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "881eefbe-f2a5-4646-abb3-c3b74500e94b",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "96f38f41-74dd-4483-a65c-89f2926bd399",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "157e63f4-ba1e-4b3e-9852-bc03eb70087d",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "67ef7c06-d6a8-46fa-9b97-3aa7ea7eca5b",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "37434995-4e63-4c10-ad4c-d19342ed1caa",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "f312dfdf-6d50-42ed-898f-024e45726e7a",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "ac2854b7-ecb2-4451-b683-ff303e98b605",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "517052fe-383b-4c69-97ef-2a7c850e6429",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "ebcfcb8e-7e70-4e05-a0a5-e50b561158d2",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "d922c670-e4c9-4b84-9601-c5f9ec5f3a87",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "b545182f-9443-4a03-a212-95b7d6083067",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "c97235e4-3aab-499c-8b45-9b0c0a2e9a4b",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "e213cc8c-7356-40f7-bef6-9fbadc44efc7",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "1221e7d1-1852-4e8e-9d15-bc29255abb1d",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "372c4622-1b84-4c48-980e-9c42b03ca30b",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "68686864-8ba4-460c-9d89-a7e6b95309ba",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "58c04ea5-b601-4af4-ab83-0e89b7387e15",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "d59ca1b7-3ce9-4053-956b-44d4c0977500",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "cbc1e014-8d1f-434d-8a6b-34bb6128eb4a",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "04535e24-3fb5-4e77-b188-8cf979da47ef",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "736887db-c0b6-459f-af0a-4e6d6a568de2",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }, {
            "changeType": "itemAttrChanged",
            "itemId": "f25baf81-2fc3-4e2d-940b-b50453ade9c0",
            "attributeName": "sealed_days",
            "attributeValue": 0
        }],
        "profileCommandRevision": 24007,
        "serverTime": "2022-12-29T05:43:30.810Z",
        "responseVersion": 1
    })


# https://wex-public-service-live-prod.ol.epicgames.com/wex/api/game/v2/profile/ec0ebb7e56f6454e86c62299a7b32e21/SendGiftPoints?profileId=profile0&rvn=99999
@app.route("/wex/api/game/v2/profile/<accountId>/SendGiftPoints", methods=["POST"])
async def send_gift_points(request, accountId: str):
    """
    Handles the send gift point request
    :param request: The request object
    :param accountId: The account id
    :return: The response object
    """
    return sanic.response.json({
        "profileRevision": 39840,
        "profileId": "profile0",
        "profileChangesBaseRevision": 39838,
        "profileChanges": [{
            "changeType": "statModified",
            "name": "activity",
            "value": {
                "a": {
                    "date": "2022-12-28T00:00:00.000Z",
                    "claimed": False,
                    "props": {
                        "BaseBonus": 10
                    }
                },
                "b": {
                    "date": "2022-12-27T00:00:00.000Z",
                    "claimed": True,
                    "props": {
                        "BaseBonus": 10,
                        "EnergySpent": 3
                    }
                },
                "standardGift": 10
            }
        }],
        "profileCommandRevision": 23699,
        "serverTime": "2022-12-28T11:37:06.741Z",
        "multiUpdate": [{
            "profileRevision": 9864,
            "profileId": "friends",
            "profileChangesBaseRevision": 9862,
            "profileChanges": [],
            "profileCommandRevision": 8247
        }],
        "responseVersion": 1
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8889, auto_reload=True, debug=True)
