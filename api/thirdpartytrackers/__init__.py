"""
Handles the silly 3rd party trackers
"""
import sanic
from .adjust import adjust
from .appflyer import appflyer

trackers = sanic.Blueprint.group(adjust, appflyer)
