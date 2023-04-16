"""
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
from .profile.abandon_level import wex_profile_abandon_level
from .profile.add_epic_friend import wex_profile_add_epic_friend
from .profile.add_to_monster_pit import wex_profile_add_to_monster_pit
from .profile.blitz_level import wex_profile_blitz_level
from .profile.bulk_improve_heroes import wex_profile_bulk_improve_heroes
from .profile.buy_back_from_monster_pit import wex_profile_buy_back_from_monster_pit
from .profile.cash_out_workshop import wex_profile_cash_out_workshop
from .profile.claim_account_reward import wex_profile_claim_account_reward
from .profile.claim_event_rewards import wex_profile_claim_event_rewards
from .profile.claim_login_reward import wex_profile_claim_login
from .profile.claim_notification_optin_reward import wex_profile_claim_notification_opt_in_reward
from .profile.claim_quest_reward import wex_profile_claim_quest_reward
from .profile.claim_territory import wex_profile_claim_territory
from .profile.client_tracked_retention_analytics import wex_profile_client_tracked_retention_analytics
from .profile.evolve_hero import wex_profile_evolve_hero
from .profile.finalize_level import wex_profile_finalize_level
from .profile.foil_hero import wex_profile_foil_hero
from .profile.generate_daily_quests import wex_profile_generate_daily_quests
from .profile.generate_match_with_friend import wex_profile_generate_match_with_friend
from .profile.initialize_level import wex_profile_initialize_level
from .profile.join_matchmaking import wex_profile_join_matchmaking
from .profile.level_up_hero import wex_profile_level_up_hero
from .profile.mark_item_seen import wex_profile_mark_item_seen
from .profile.modify_hero_armor import wex_profile_modify_hero_armor
from .profile.modify_hero_gear import wex_profile_modify_hero_gear
from .profile.modify_hero_weapon import wex_profile_modify_hero_weapon
from .profile.open_gift_box import wex_profile_open_gift_box
from .profile.open_hero_chest import wex_profile_open_hero_chest
from .profile.pick_hero_chest import wex_profile_pick_hero_chest
from .profile.promote_hero import wex_profile_promote_hero
from .profile.purchase_catalog_entry import wex_profile_purchase_catalog_entry
from .profile.query_profile import wex_profile_query
from .profile.reconcile import wex_profile_reconcile
from .profile.remove_from_monster_pit import wex_profile_remove_from_monster_pit
from .profile.roll_hammer_chests import wex_profile_roll_hammer_chests
from .profile.select_hammer_chest import wex_profile_select_hammer_chest
from .profile.select_start_options import wex_profile_select_start_options
from .profile.sell_hero import wex_profile_sell_hero
from .profile.send_gift_points import wex_profile_send_gift
from .profile.set_default_party import wex_profile_set_default_party
from .profile.set_rep_hero import wex_profile_set_rep_hero
from .profile.suggestion_response import wex_profile_suggestion_response
from .profile.tap_hammer_chest import wex_profile_tap_hammer_chest
from .profile.unlock_armor_gear import wex_profile_unlock_armor_gear
from .profile.unlock_hero_gear import wex_profile_unlock_hero_gear
from .profile.unlock_region import wex_profile_unlock_region
from .profile.unlock_weapon_gear import wex_profile_unlock_weapon_gear
from .profile.update_friends import wex_profile_update_friends
from .profile.update_monster_pit_power import wex_profile_update_monster_pit_power
from .profile.update_party import wex_profile_update_party
from .profile.upgrade_building import wex_profile_upgrade_building
from .profile.upgrade_hero import wex_profile_upgrade_hero
from .profile.upgrade_hero_skills import wex_profile_upgrade_hero_skills
from .profile.verify_real_money_purchase import wex_verify_realmoney
from .profile.update_account_headless_status import wex_update_headless

wex = sanic.Blueprint.group(wex_log, wex_entitlement, wex_catalog, wex_timeline, wex_version_check, wex_version_probe,
                            wex_cloud, wex_item_ratings, wex_profile_abandon_level, wex_profile_add_epic_friend,
                            wex_profile_add_to_monster_pit, wex_profile_blitz_level, wex_profile_bulk_improve_heroes,
                            wex_profile_buy_back_from_monster_pit, wex_profile_cash_out_workshop,
                            wex_profile_claim_account_reward, wex_profile_claim_event_rewards, wex_profile_claim_login,
                            wex_profile_claim_notification_opt_in_reward, wex_profile_claim_quest_reward,
                            wex_profile_claim_territory, wex_profile_client_tracked_retention_analytics,
                            wex_profile_evolve_hero, wex_profile_finalize_level, wex_profile_foil_hero,
                            wex_profile_generate_daily_quests, wex_profile_generate_match_with_friend,
                            wex_profile_initialize_level, wex_profile_join_matchmaking, wex_profile_level_up_hero,
                            wex_profile_mark_item_seen, wex_profile_modify_hero_armor, wex_profile_modify_hero_gear,
                            wex_profile_modify_hero_weapon, wex_profile_open_gift_box, wex_profile_open_hero_chest,
                            wex_profile_pick_hero_chest, wex_profile_promote_hero, wex_profile_purchase_catalog_entry,
                            wex_profile_query, wex_profile_reconcile, wex_profile_remove_from_monster_pit,
                            wex_profile_roll_hammer_chests, wex_profile_select_hammer_chest,
                            wex_profile_select_start_options, wex_profile_sell_hero, wex_profile_send_gift,
                            wex_profile_set_default_party, wex_profile_set_rep_hero, wex_profile_suggestion_response,
                            wex_profile_tap_hammer_chest, wex_profile_unlock_armor_gear, wex_profile_unlock_hero_gear,
                            wex_profile_unlock_region, wex_profile_unlock_weapon_gear, wex_profile_update_friends,
                            wex_profile_update_monster_pit_power, wex_profile_update_party,
                            wex_profile_upgrade_building, wex_profile_upgrade_hero, wex_profile_upgrade_hero_skills,
                            wex_receipts, wex_manifest, wex_verify_realmoney, wex_update_headless)
