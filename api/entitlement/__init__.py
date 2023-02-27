"""
Handles the entitlement check for the launcher
"""
import sanic
from .entitlement import entitlement

datarouter = sanic.Blueprint.group(entitlement)
