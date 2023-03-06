"""
Handles the cdn for battle breakers
"""
import sanic
from .manifest import manifest

bb_cdn = sanic.Blueprint.group(manifest)
