"""
Handles the price engine for calculating tax
"""
import sanic
from .price import price

priceengine = sanic.Blueprint.group(price)
