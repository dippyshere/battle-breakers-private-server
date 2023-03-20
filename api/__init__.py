"""
Main Blueprint group for the server
"""
import sanic
from .thirdpartytrackers import trackers
from .account import account
# from .battlebreakers import bb_cdn
from .catalog import catalog
from .datarouter import datarouter
from .entitlement import entitlement
from .friends import friends
from .lightswitch import lightswitch
from .priceengine import priceengine
from .wex import wex

api = sanic.Blueprint.group(trackers, account, catalog, datarouter, entitlement, friends, lightswitch, priceengine, wex)
