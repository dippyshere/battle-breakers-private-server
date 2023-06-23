"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the account related requests
"""
import sanic
from .accountInfo import account_info
from .externalAuths import external_auths
from .kill import kill
from .metadata import account_metadata
from .publicAccount import public_account
from .quickstart import account_quickstart
from .ssodomains import ssodomains
from .token import token
from .verify import verify
from .deviceAuth import device_auth
from .exchange import exchange
from .version import account_version

from middleware.account_middleware import include_perms

account = sanic.Blueprint.group(account_info, external_auths, kill, public_account, account_quickstart, ssodomains,
                                token, verify, device_auth, exchange, account_version, account_metadata,
                                url_prefix="/account")

account.middleware("response", priority=99)(include_perms)
