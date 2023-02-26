"""
Handles the service status for Battle Breakers
"""
import sanic
from .status import status

lightswitch = sanic.Blueprint.group(status)
