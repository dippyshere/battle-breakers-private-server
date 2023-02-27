"""
Main Blueprint group for the server
"""
import sanic
from .account import account
from .catalog import catalog
from .datarouter import datarouter
from .entitlement import entitlement
from .friends import friends
from .lightswitch import lightswitch
from .priceengine import priceengine
from .wex import wex

api = sanic.Blueprint.group(account, catalog, datarouter, entitlement, friends, lightswitch, priceengine, wex)
