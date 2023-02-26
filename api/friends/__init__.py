"""
Handles the friend requests
"""
import sanic
from .summary import summary

friends = sanic.Blueprint.group(summary)
