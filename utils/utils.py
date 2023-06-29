"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

This file contains utility functions for the server
"""

import base64
import datetime
import functools
import os
import random
import re
import uuid
import zlib
from inspect import isawaitable
from typing import Any, Tuple, Optional, Callable

import jwt
import orjson
import sanic
import aiofiles

from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.backends import default_backend

from utils.exceptions import errors

# Load the private key
with open('utils/crypto/bb_private_key.pem', 'rb') as f:
    private_key_data = f.read()
    private_key = load_pem_private_key(private_key_data, password=b'wex_dippy_server', backend=default_backend())

with open('utils/crypto/bb_public_key.pem', 'rb') as f:
    public_key_data = f.read()
    public_key = load_pem_public_key(public_key_data, backend=default_backend())


async def read_file(filename: str, json: bool = True, raw: bool = True) -> dict | bytes | str:
    """
    Reads a file and returns the contents
    :param filename: The file to read
    :param json: Whether to parse the file as json
    :param raw: Whether to read the file as bytes
    :return: The contents of the file
    """
    if json:
        async with aiofiles.open(filename, "rb") as file:
            return orjson.loads((await file.read()))
    if raw:
        async with aiofiles.open(filename, "rb") as file:
            return await file.read()
    async with aiofiles.open(filename, "r") as file:
        return await file.read()


async def write_file(filename: str, contents: Any, json: bool = True, raw: bool = True) -> None:
    """
    Writes to a file
    :param filename: The file to write to
    :param contents: The contents to write
    :param json: Whether to write the contents as json
    :param raw: Whether to write the contents as bytes
    """
    if json:
        async with aiofiles.open(filename, "wb") as file:
            await file.write(orjson.dumps(contents))
        return
    if raw:
        async with aiofiles.open(filename, "wb") as file:
            await file.write(contents)
        return
    async with aiofiles.open(filename, "w") as file:
        await file.write(contents)
    return


async def format_time(time: Optional[datetime.datetime | float | int | str] = None) -> str:
    """
    Formats the current time in the correct format for the MCP headers

    :param time: The time to format
    :return: The formatted time string in the format of YYYY-MM-DDTHH:MM:SS.mmmZ (ISO8601)
    """
    if time is None:
        return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    else:
        if isinstance(time, datetime.datetime):
            return time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        # elif isinstance(time, float) or isinstance(time, int):
        #     return datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        elif isinstance(time, str):
            return datetime.datetime.fromisoformat(time).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        else:
            return datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


async def get_nearest_12_hour_interval() -> datetime.datetime:
    """
    Gets the nearest 12 hour interval from the current time
    :return:
    """
    next_12hr = datetime.datetime.utcnow() + datetime.timedelta(hours=12 - (datetime.datetime.utcnow().hour % 12))
    return datetime.datetime(next_12hr.year, next_12hr.month, next_12hr.day, next_12hr.hour,
                             tzinfo=datetime.timezone.utc)


async def get_current_12_hour_interval() -> datetime.datetime:
    """
    Gets the current 12 hour interval
    :return:
    """
    current_12hr = datetime.datetime.utcnow() - datetime.timedelta(hours=datetime.datetime.utcnow().hour % 12)
    return datetime.datetime(current_12hr.year, current_12hr.month, current_12hr.day, current_12hr.hour,
                             tzinfo=datetime.timezone.utc)


async def token_generator() -> str:
    """
    Generates 16 random bytes, converted to hex
    :return: The generated string
    """
    # return ''.join(random.choice(chars).lower() for _ in range(size))
    return uuid.UUID(bytes=random.randbytes(16)).hex


async def generate_eg1(sub: Optional[str] = None, dn: Optional[str] = None, clid: Optional[str] = None,
                       dvid: Optional[str] = None) -> str:
    """
    Generates an eg1 JWT token for an account
    :param sub: The account id to generate the token for
    :param dn: The display name of the account
    :param clid: The client id of the account
    :param dvid: The device id of the account
    :return: The JWT token
    """
    if sub is None:
        sub = await token_generator()
    if clid is None:
        clid = "3cf78cd3b00b439a8755a878b160c7ad"
    if dvid is None:
        dvid = await token_generator()
    p = f"wexp:cloudstorage:system=2,account:public:account:*=2,xmpp:session:*:{sub}=1,wexp:push:devices:{sub}=15," \
        f"account:oauth:exchangeTokenCode=15,account:public:account=2,priceengine:shared:offer:price=2," \
        f"wexp:wexp_role:client=15,account:public:account:externalAuths=15,wexp:calendar=2,blockList:{sub}=14," \
        f"account:token:otherSessionsForAccountClient=8,friends:{sub}=15," \
        f"account:token:otherSessionsForAccountClientService=8,wexp:profile:{sub}:*=15," \
        f"account:public:account:deviceAuths=11,wexp:cloudstorage:system:*=2,serviceinstance=2,wexp:storefront=2"
    headers = {"alg": "RS256", "kid": str(uuid.uuid4())}
    return jwt.encode({
        "sub": sub,
        "dvid": dvid,
        "mver": False,
        "clid": clid,
        "dn": dn,
        "am": "exchange_code",
        "p": base64.b64encode(zlib.compress(p.encode())).decode(),
        "iai": sub,
        "sec": 1,
        "clsvc": "wex",
        "t": "s",
        "ic": True,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8),
        "iat": datetime.datetime.utcnow(),
        "jti": await token_generator()
    }, private_key, "RS256", headers)


async def generate_client_eg1(clid: Optional[str] = None) -> str:
    """
    Generates an eg1 JWT token for client credentials
    :param clid: The client id to generate the token for
    :return: The JWT token
    """
    if clid is None:
        clid = "3cf78cd3b00b439a8755a878b160c7ad"
    headers = {"alg": "RS256", "kid": str(uuid.uuid4())}
    return jwt.encode({
        "p": "eNp9zDEOgzAMheH7VCxltMTQE/QMxnEgkomR4wi4fQMS3drRz/r+jfcVCIVzQBv6jtBRdIIyo3EAjZGttB2JtGaHtY6SCO6Td2fLKK"
             "/q8zvLMTy77SqK1lBcDSeGchTn5Wfkj4HHqWJMktD56+6hPS95Io6mrdV/AKLsT2A=",
        "clsvc": "wex",
        "t": "s",
        "mver": False,
        "clid": clid,
        "ic": True,
        "am": "client_credentials",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=4),
        "iat": datetime.datetime.utcnow(),
        "jti": await token_generator()
    }, private_key, "RS256", headers)


async def generate_refresh_eg1(sub: Optional[str] = None, dn: Optional[str] = None, clid: Optional[str] = None,
                               dvid: Optional[str] = None) -> str:
    """
    Generates an eg1 JWT token for an account
    :param sub: The account id to generate the token for
    :param dn: The display name of the account
    :param clid: The client id of the account
    :param dvid: The device id of the account
    :return: The JWT token
    """
    if sub is None:
        sub = await token_generator()
    if clid is None:
        clid = await token_generator()
    if dvid is None:
        dvid = await token_generator()
    headers = {"alg": "RS256", "kid": str(uuid.uuid4())}
    return jwt.encode({
        "sub": sub,
        "dvid": dvid,
        "t": "r",
        "clid": clid,
        "dn": dn,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=672),
        "am": "exchange_code",
        "jti": await token_generator()
    }, private_key, "RS256", headers)


async def generate_authorisation_eg1(sub: Optional[str] = None, dn: Optional[str] = None,
                                     clid: Optional[str] = None) -> str:
    """
    Generates an eg1 JWT token for an account to use as an auth code
    :param sub: The account id to generate the token for
    :param dn: The display name of the account
    :param clid: The client id of the account
    :return: The JWT token
    """
    if sub is None:
        sub = await token_generator()
    if clid is None:
        clid = await token_generator()
    headers = {"alg": "RS256", "kid": str(uuid.uuid4())}
    return jwt.encode({
        "sub": sub,
        "t": "r",
        "clid": clid,
        "dn": dn,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8),
        "am": "exchange_code",
        "jti": await token_generator()
    }, private_key, "RS256", headers)


async def parse_eg1(token: str) -> Optional[dict]:
    """
    Parses an eg1 JWT token
    :param token: The token to parse
    :return: The parsed token
    """
    try:
        token = token.replace("bearer ", "").replace("eg1~", "")
        return jwt.decode(token, public_key, algorithms=["RS256"], leeway=20)
    except:
        return None


async def verify_owner(request: sanic.request.Request, token: dict) -> bool:
    """
    Verifies that the owner of the token is the owner of the account
    :param request: The request to verify
    :param token: The token to verify
    :return: True if the token is the owner of the account, False otherwise
    """
    account_id = request.match_info.get('accountId')
    if account_id is None:
        account_id = request.form.get("accountId")
    if account_id is None:
        account_id = request.args.get("accountId")
    if account_id is None:
        try:
            account_id = request.json.get("accountId")
        except:
            pass
    if account_id is None:
        return False
    if token.get("sub") != account_id:
        return False
    return True


async def verify_request_auth(request: sanic.request.Request, strict: bool = False) -> bool:
    """
    Verifies the authorisation of a request
    :param request: The request to verify
    :param strict: Whether to be strict about account id
    :return: True if the request is authorised, False otherwise
    """
    try:
        if request.headers.get("Authorization", "").startswith("bearer "):
            token = request.headers.get("Authorization", "").replace("bearer ", "").replace("eg1~", "")
            token = jwt.decode(token, public_key, algorithms=["RS256"], leeway=20)
            if strict:
                if not (await verify_owner(request, token)):
                    raise errors.com.epicgames.account.auth_app.not_authorized_for_account()
            else:
                request.ctx.is_owner = await verify_owner(request, token)
            request.ctx.owner = token.get("sub")
            request.ctx.dvid = token.get("dvid")
            return True
        else:
            return False
    except:
        return False


def authorized(maybe_func: Any = None, *, allow_basic: bool = False, strict: bool = False) -> Callable:
    """
    Decorator to check if a request is authorized
    :return: The decorator
    """

    def decorator(f: Callable) -> Callable:
        """
        The decorator
        :param f: The function to decorate
        :return: The decorated function
        """

        @functools.wraps(f)
        async def decorated_function(request: sanic.request.Request, *args,
                                     **kwargs) -> sanic.response.HTTPResponse | sanic.response.JSONResponse:
            """
            The decorated function

            :param request: The request object
            :param args: Arguments to pass to the function
            :param kwargs: Keyword arguments to pass to the function
            :return: The response
            """
            if allow_basic:
                if request.headers.get("Authorization", "").startswith("basic "):
                    try:
                        token = request.headers.get("Authorization", "").replace("basic ", "")
                        token = base64.b64decode(token).decode()
                        if token[32] == ":":
                            is_authorised = True
                        else:
                            raise Exception()
                    except:
                        is_authorised = False
                else:
                    is_authorised = await verify_request_auth(request, strict)
            else:
                is_authorised = await verify_request_auth(request, strict)

            if is_authorised:
                # the user is authorised
                # run the handler method and return the response
                response = f(request, *args, **kwargs)
                if isawaitable(response):
                    response = await response
                return response
            else:
                # the user is not authorised
                raise sanic.exceptions.Forbidden("Authentication failed :/", context={
                    "errorCode": "errors.com.epicgames.common.authentication.authentication_failed",
                    "errorMessage": "Your authentication has expired. Please log in again."})

        return decorated_function

    return decorator(maybe_func) if maybe_func else decorator


async def to_insecure_hash(s: str) -> int:
    """
    Hashes a string
    :param s: The string to hash
    :return: The hash of the string as an integer
    """
    hash_val = 0
    for c in s:
        hash_val = ((hash_val << 5) - hash_val) + ord(c)
        hash_val &= 0xffffffff  # Convert to 32-bit integer
    return hash_val


async def get_account_id_from_display_name(display_name: str) -> Optional[str]:
    """
    Gets an account id from a display name
    :param display_name: The display name to get the account id for
    :return: The account id
    """
    display_name = display_name.lower()
    for file in os.listdir("res/account/api/public/account/"):
        if file.endswith(".json"):
            data = await read_file(f"res/account/api/public/account/{file}")
            if data.get("displayName") is not None:
                if data["displayName"].lower() == display_name:
                    return data["id"]
    return None


async def get_account_id_from_email(email: str) -> Optional[str]:
    """
    Gets an account id from an email
    :param email: The email to get the account id for
    :return: The account id
    """
    for file in os.listdir("res/account/api/public/account/"):
        if file.endswith(".json"):
            data = await read_file(f"res/account/api/public/account/{file}")
            if data["email"].split("@")[0] == email.split("@")[0]:
                return data["id"]
    return None


async def check_if_display_name_exists(display_name: str) -> bool:
    """
    Checks if a display name exists
    :param display_name: The display name to check
    :return: True if the display name exists, False otherwise
    """
    for file in os.listdir("res/account/api/public/account/"):
        if file.endswith(".json"):
            data = await read_file(f"res/account/api/public/account/{file}")
            if data["displayName"] == display_name:
                return True
    return False


async def oauth_response(client_id: str = "3cf78cd3b00b439a8755a878b160c7ad", dn: Optional[str] = None,
                         dvid: Optional[str] = None, sub: Optional[str] = None) -> dict:
    """
    Generates an oauth response
    :param client_id: The client id
    :param dn: The display name
    :param dvid: The device id
    :param sub: The account ID
    :return: The oauth response
    """
    return {
        "access_token": f"eg1~{await generate_eg1(sub, dn, client_id, dvid)}",
        "expires_in": 28800,
        "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M"
                                                                                          ":%S.000Z"),
        "token_type": "bearer",
        "refresh_token": f"eg1~{await generate_refresh_eg1(sub, dn, client_id, dvid)}",
        "refresh_expires": 2419200,
        "refresh_expires_at": await format_time(datetime.datetime.utcnow() + datetime.timedelta(hours=672)),
        "account_id": sub,
        "client_id": client_id,
        "internal_client": True,
        "client_service": "wex",
        "displayName": dn,
        "app": "wex",
        "in_app_id": sub,  # backwards compatability with soft-launch wex clients (circa 2017)
        "device_id": dvid
    }


async def oauth_client_response(client_id: str) -> dict:
    """
    Generates an oauth response for a client
    :param client_id: The client id
    :return: The oauth response
    """
    return {
        "access_token": f"eg1~{await generate_client_eg1(client_id)}",
        "expires_in": 14400,
        "expires_at": await format_time(datetime.datetime.utcnow() + datetime.timedelta(hours=4)),
        "token_type": "bearer",
        "client_id": client_id,
        "internal_client": True,
        "client_service": "wex",
        "scope": [],
        "app": "wex"
    }


async def create_account(displayName: Optional[str] = None, password: Optional[str | int] = None) -> str:
    """
    Creates an account and prepares all the files
    :param displayName: The display name
    :param password: The password hash
    :return: The account id
    """
    from utils import account_initialisation
    account_id = await account_initialisation.initialise_account(None, displayName, password)
    return account_id


async def normalise_string(input_string: Optional[str]) -> Optional[str]:
    """
    Normalises a string
    :param input_string: The string to normalise
    :return: The normalised string
    """
    if input_string is not None:
        normalised_string = ''.join(char.upper() for char in input_string if char.isalpha())
        return normalised_string
    return ""


async def load_datatable(datatable: Optional[str]) -> Optional[dict]:
    """
    Loads a datatable. As datatables are both static and large, this could be cached, but async cache sucks :(
    :param datatable: The datatable path to load
    :return: The datatable
    """
    if datatable is not None:
        return await read_file(f"res/Game/WorldExplorers/{datatable}.json")
    return None


async def get_template_id_from_path(path: Optional[str]) -> Optional[str]:
    """
    Gets a template id from a path
    :param path: The path to get the template id for
    :return: The template id
    """
    if path is not None:
        # I hope you love this, remaps paths from old versions to new versions
        if path in ['/Game/Loot/AccountItems/Vouchers/Voucher_HeroSilver.Voucher_HeroSilver',
                    '/Game/Loot/AccountItems/Reagents/Reagent_Hero_Silver.Reagent_Hero_Silver',
                    '/Game/Loot/AccountItems/Reagents/Reagent_Hero_Gold.Reagent_Hero_Gold',
                    '/Game/Loot/AccountItems/Reagents/Reagent_Hero_Diamond.Reagent_Hero_Diamond',
                    '/Game/Loot/AccountItems/Vouchers/Voucher_HeroBronze.Voucher_HeroBronze',
                    '/Game/Loot/AccountItems/Tokens/TK_Voucher_HeroSilver.TK_Voucher_HeroSilver',
                    '/Game/Loot/AccountItems/Tokens/TK_Voucher_HeroGold.TK_Voucher_HeroGold']:
            path = '/Game/Loot/AccountItems/Tokens/TK_HeroMap_Elemental.TK_HeroMap_Elemental'
        elif path == '/Game/Loot/AccountItems/Reagents/Reagent_Hero_Diamond.Reagent_Hero_Diamond':
            path = '/Game/Loot/AccountItems/Tokens/TK_HeroMap_SuperRare.TK_HeroMap_SuperRare'
        elif path == '/Game/Loot/AccountItems/TreasureMaps/TM_PortalResource.TM_PortalResource':
            path = '/Game/Loot/AccountItems/TreasureMaps/TM_MapResource.TM_MapResource'
        elif path in ['/Game/Loot/AccountItems/Reagents/Reagent_Dark_T05.Reagent_Dark_T05',
                      '/Game/Loot/AccountItems/Reagents/Reagent_Dark_T04.Reagent_Dark_T04']:
            path = '/Game/Loot/AccountItems/Reagents/Reagent_Shard_Dark.Reagent_Shard_Dark'
        elif path in ['/Game/Loot/AccountItems/Reagents/Reagent_Fire_T05.Reagent_Fire_T05',
                      '/Game/Loot/AccountItems/Reagents/Reagent_Fire_T04.Reagent_Fire_T04']:
            path = '/Game/Loot/AccountItems/Reagents/Reagent_Shard_Fire.Reagent_Shard_Fire'
        elif path in ['/Game/Loot/AccountItems/Reagents/Reagent_Light_T05.Reagent_Light_T05',
                      '/Game/Loot/AccountItems/Reagents/Reagent_Light_T04.Reagent_Light_T04']:
            path = '/Game/Loot/AccountItems/Reagents/Reagent_Shard_Light.Reagent_Shard_Light'
        elif path in ['/Game/Loot/AccountItems/Reagents/Reagent_Nature_T05.Reagent_Nature_T05',
                      '/Game/Loot/AccountItems/Reagents/Reagent_Nature_T04.Reagent_Nature_T04']:
            path = '/Game/Loot/AccountItems/Reagents/Reagent_Shard_Nature.Reagent_Shard_Nature'
        elif path in ['/Game/Loot/AccountItems/Reagents/Reagent_Water_T05.Reagent_Water_T05',
                      '/Game/Loot/AccountItems/Reagents/Reagent_Water_T04.Reagent_Water_T04']:
            path = '/Game/Loot/AccountItems/Reagents/Reagent_Shard_Water.Reagent_Shard_Water'
        elif path == '/Game/Loot/AccountItems/Ore/Ore_CrystalShard.Ore_CrystalShard':
            path = '/Game/Loot/AccountItems/Ore/Ore_Magicite.Ore_Magicite'
        path = path.replace("/Game", "WorldExplorers/Content").split(".")[0].replace("WorldExplorers/",
                                                                                     "res/Game/WorldExplorers/")
        data = await read_file(f"{path}.json")
        if data[0].get('Type') == "WExpGenericAccountItemDefinition":
            return f"{data[0].get('Properties').get('ItemType').split('::')[-1]}:{data[0].get('Name')}"
        if data[0].get('Type') == "WExpCharacterDefinition":
            return f"Character:{data[0].get('Name').split('CD_')[-1]}"
        if data[0].get('Type') == "WExpVoucherItemDefinition":
            return f"Voucher:{data[0].get('Name')}"
        if data[0].get('Type') == "WExpUpgradePotionDefinition":
            return f"UpgradePotion:{data[0].get('Name')}"
        if data[0].get('Type') == "WExpXpBookDefinition":
            return "Currency:HeroXp_Basic"  # hardcoded as in newer versions, all xp books are one type
        if data[0].get('Type') == "WExpTreasureMapDefinition":
            return f"TreasureMap:{data[0].get('Name')}"
        if data[0].get('Type') == "WExpTokenDefinition":
            return f"Token:{data[0].get('Name')}"
    return None


async def extract_version_info(user_agent: str) -> Tuple[int, int, int]:
    """
    Extracts the version info from a user agent
    :param user_agent: The user agent to extract the version info from
    :return: The version info as a tuple of (minor_version, revision, changelist)
    """
    modern_version_regex = r"1\.(\d*)\.(\d*)-r(\d*)"
    legacy_version_regex = r"-(\d*)\+\+\+WEX\+Release-1\.(\d*)"
    ultra_legacy_version_regex = r"-(\d*)\+\+\+WEX\+Release-(\d*)"
    ultra_legacy_version_regex_2 = r"Release-(\d*)-CL-(\d*)"
    match = re.search(modern_version_regex, user_agent)
    if match:
        minor_version = int(match.group(1))
        revision = int(match.group(2))
        changelist = int(match.group(3))
        return minor_version, revision, changelist
    match = re.search(legacy_version_regex, user_agent)
    if match:
        minor_version = int(match.group(2))
        revision = 0
        changelist = int(match.group(1))
        return minor_version, revision, changelist
    match = re.search(ultra_legacy_version_regex, user_agent)
    if match:
        minor_version = 0
        revision = int(match.group(2))
        changelist = int(match.group(1))
        return minor_version, revision, changelist
    match = re.search(ultra_legacy_version_regex_2, user_agent)
    if match:
        minor_version = 0
        revision = int(match.group(1))
        changelist = int(match.group(2))
        return minor_version, revision, changelist
    return 88, 244, 17036752  # Default values if no match is found


async def room_generator(level_id: str, room_number: int, level_info: dict) -> dict:
    """
    Generates a room based on the level info
    :param level_id: The level id to generate the room for
    :param room_number: The room number to generate
    :param level_info: The level info from the datatable
    :return: The generated room as a dict to append to level notification
    """
    room_name = "Room.Unique.ForestOfMixedEmotions.Map1.R01"
    room_info = (await load_datatable("Content/World/Datatables/LevelRooms"))[0]["Rows"].get(room_name)
    room = {
        "roomName": room_name,
        "regionName": level_id,
        "depth": room_number,
        "worldLevel": level_info["BaseWorldLevel"],
        "discoveryGoldMult": room_info["GoldDropMult"],
        "occupants": [{
            "isFriendly": False,
            "characterTemplateId": "Character:Assassin_C1_Dark_ImpStab_T01",
            "spawnGroup": [],
            "killXp": 1,
            "spawnClass": "Normal",
            "lootQuantity": 0
        }, {
            "isFriendly": False,
            "characterTemplateId": "Character:Mage_Basic_Fire_Sprite_T01",
            "spawnGroup": [],
            "killXp": 1,
            "spawnClass": "Normal",
            "lootQuantity": 0
        }, {
            "isFriendly": False,
            "characterTemplateId": "Character:Mage_Basic_Nature_Sprite_T01",
            "spawnGroup": [],
            "killXp": 1,
            "spawnClass": "Normal",
            "lootQuantity": 0
        }, {
            "isFriendly": False,
            "characterTemplateId": "Character:Mage_Basic_Water_Sprite_T01",
            "spawnGroup": [],
            "killXp": 1,
            "spawnClass": "Normal",
            "lootQuantity": 0
        }, {
            "isFriendly": False,
            "characterTemplateId": "Character:Ninja_Basic_Nature_Flurry_T02",
            "spawnGroup": [],
            "killXp": 2,
            "spawnClass": "Normal",
            "lootQuantity": 0
        }, {
            "isFriendly": False,
            "characterTemplateId": "Character:AI_PoisonTank_Nature_Tutorial",
            "spawnGroup": [{
                "isFriendly": False,
                "characterTemplateId": "Character:Warrior_UC1_Nature_LesserDemon_T03",
                "killXp": 12,
                "spawnClass": "BossMedium",
                "lootTemplateId": "Currency:HeroXp_Basic",
                "lootQuantity": 2249
            }],
            "killXp": 24,
            "spawnClass": "BossMedium",
            "lootTemplateId": "Currency:Gold",
            "lootQuantity": 58
        }, {
            "isFriendly": False,
            "killXp": 0,
            "lootTemplateId": "Currency:Gold",
            "lootQuantity": 15
        }, {
            "isFriendly": False,
            "killXp": 0,
            "lootTemplateId": "Currency:Gold",
            "lootQuantity": 11
        }, {
            "isFriendly": False,
            "killXp": 0,
            "lootTemplateId": "Item:HealthVial",
            "lootQuantity": 1
        }, {
            "isFriendly": False,
            "killXp": 0,
            "lootTemplateId": "Container:Chest_Water_Low",
            "lootQuantity": 1
        }]
    }
    return room
