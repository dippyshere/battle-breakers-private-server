"""
Handles the eula tracking
"""
import sanic
from .agreements import agreements

agreements = sanic.Blueprint.group(agreements)
