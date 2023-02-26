"""
Handles the telemetry data from the client
"""
import sanic
from .data import data

datarouter = sanic.Blueprint.group(data)
