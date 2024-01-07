"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the main world explorers api backend
"""
import sanic
from .log_upload import wex_log
from .entitlement import wex_entitlement
from .catalog import wex_catalog
from .receipts import wex_receipts
from .timeline import wex_timeline
from .version_check import wex_version_check
from .version_probe import wex_version_probe
from .cloud_storage import wex_cloud
from .item_ratings import wex_item_ratings
from .manifest import wex_manifest
from .motd import wex_motd
from .version import wex_version
from .profile import wex_profile
from .enabled_features import wex_enabled_features
from .friends import wex_friend
from .push import wex_push

wex = sanic.Blueprint.group(wex_log, wex_entitlement, wex_catalog, wex_timeline, wex_version_check, wex_version_probe,
                            wex_cloud, wex_item_ratings, wex_receipts, wex_manifest, wex_motd, wex_version, wex_profile,
                            wex_enabled_features, wex_friend, wex_push, url_prefix="/wex")
