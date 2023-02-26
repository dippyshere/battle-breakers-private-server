"""
Handles the catalog endpoints
"""
import sanic
from .bulk import bulk
from .namespace import namespace

catalog = sanic.Blueprint.group(bulk, namespace)
