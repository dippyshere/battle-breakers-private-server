"""
Handles the price engine for calculating tax
"""
import sanic
from .log_upload import wex_log
from .entitlement import wex_entitlement
from .catalog import wex_catalog
from .timeline import wex_timeline
from .version_check import wex_version_check
from .version_probe import wex_version_probe
from .cloud_storage import wex_cloud

wex = sanic.Blueprint.group(wex_log, wex_entitlement, wex_catalog, wex_timeline, wex_version_check, wex_version_probe,
                            wex_cloud)
