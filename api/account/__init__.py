"""
Handles the account requests
"""
import sanic
from .accountInfo import account_info
from .externalAuths import external_auths
from .kill import kill
from .publicAccount import public_account
from .ssodomains import ssodomains
from .token import token
from .verify import verify

account = sanic.Blueprint.group(account_info, external_auths, kill, public_account, ssodomains, token, verify)
