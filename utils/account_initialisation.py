"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

This file creates the base version of all necessary files for an account.
"""
import datetime
import os
import uuid

from utils.utils import normalise_string, write_file


async def initialise_account(account_id: str = None, display_name: str = None, password: str | int = None,
                             **kwargs) -> str:
    """
    Initialises an account with the given account ID.
    :param account_id: The account ID to initialise
    :param display_name: The display name to use
    :param password: The password to use
    :param kwargs: Any other arguments to use
    :return: account_id
    """
    from utils.utils import token_generator
    from utils.utils import format_time
    if account_id is None:
        while True:
            # this should only really happen once
            account_id = await token_generator()
            if not os.path.exists(f"res/account/api/public/account/{account_id}.json"):
                break
    # create the directories
    os.makedirs(f"res/account/api/public/account", exist_ok=True)
    os.makedirs(f"res/friends/api/v1", exist_ok=True)
    os.makedirs(f"res/wex/api/game/v2/item_ratings", exist_ok=True)
    os.makedirs(f"res/wex/api/game/v2/profile/{account_id}/QueryProfile", exist_ok=True)
    os.makedirs(f"res/wex/api/receipts/v1/account", exist_ok=True)
    # initialise the account services
    # we don't use headless because the display name is what we ask for during sign up (to avoid asking for an email)
    # headless is used in quickstart to allow the user to set a display name
    await write_file(f"res/account/api/public/account/{account_id}.json", {
        "id": account_id,
        "displayName": display_name,
        "minorVerified": False,
        "minorStatus": "NOT_MINOR",
        "cabinedMode": False,
        "name": None,
        "email": f"{display_name}@dippy.com",
        "failedLoginAttempts": 0,
        "lastLogin": None,
        "numberOfDisplayNameChanges": 0,
        "dateOfBirth": None,
        "ageGroup": "ADULT",
        "headless": False,
        "country": None,
        "lastName": None,
        "phoneNumber": None,
        "preferredLanguage": "en",
        "lastDisplayNameChange": None,
        "canUpdateDisplayName": True,
        "tfaEnabled": False,
        "emailVerified": False,
        "minorExpected": False,
        "hasHashedEmail": False,
        "externalAuths": {},
        "extra": {
            "pwhash": password,
            "deviceAuths": []
        }
    })
    # catalog service is shared
    # initialise entitlement service
    # TODO: This could be hardcoded in the response if storage is an issue
    await write_file(f"res/entitlement/api/account/{account_id}.json", [])
    # initialise friends service
    await write_file(f"res/friends/api/v1/{account_id}.json", {
        "friends": [],
        "incoming": [],
        "outgoing": [],
        "suggested": [],
        "blocklist": [],
        "settings": {
            "acceptInvites": "public",
            "mutualPrivacy": "ALL"
        },
        "limitsReached": {
            "incoming": False,
            "outgoing": False,
            "accepted": False
        }
    })
    # price engine is shared
    # initialise wex services
    await write_file(f"res/wex/api/game/v2/item_ratings/{account_id}.json", {})
    await write_file(f"res/wex/api/game/v2/profile/{account_id}/QueryProfile/friends.json", {
        "_id": await token_generator(),
        "created": await format_time(),
        "updated": await format_time(),
        "rvn": 1,
        "wipeNumber": 4,
        "accountId": account_id,
        "profileId": "friends",
        "version": "force_max_friends_to_100",
        "items": {},
        "stats": {
            "attributes": {
                "daily_friends": {},
                "max_friend_count": 100,
                "daily_friend_uses": 2
            }
        },
        "commandRevision": 0
    })
    await write_file(f"res/wex/api/game/v2/profile/{account_id}/QueryProfile/levels.json", {
        "_id": await token_generator(),
        "created": await format_time(),
        "updated": await format_time(),
        "rvn": 1,
        "wipeNumber": 4,
        "accountId": account_id,
        "profileId": "levels",
        "version": "grant_pvp_item",
        "items": {},
        "stats": {
            "attributes": {
                "last_played_level": "",
                "last_used_friend_id": "",
                "portal_level": "",
                "personal_events": [
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 5,
                        "zoneId": "Zone.Event.PE.MidgamePet.First.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "a7604ceb-768d-4e6a-ae99-50d4286038b8",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 4,
                        "zoneId": "Zone.Event.PE.MidgamePet.Second.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "a7604ceb-768d-4e6a-ae99-50d4286038b8",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 3,
                        "zoneId": "Zone.Event.PE.MidgamePet.Third.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "a7604ceb-768d-4e6a-ae99-50d4286038b8",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 2,
                        "zoneId": "Zone.Event.PE.MidgamePet.Fourth.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "a7604ceb-768d-4e6a-ae99-50d4286038b8",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 1,
                        "zoneId": "Zone.Event.PE.MidgamePet.Fifth.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "a7604ceb-768d-4e6a-ae99-50d4286038b8",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 5,
                        "zoneId": "Zone.Event.PE.MidgameChallenge.First.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "86ad5c0f-159d-4b9c-9383-07b3dd12cd74",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 4,
                        "zoneId": "Zone.Event.PE.MidgameChallenge.Second.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "86ad5c0f-159d-4b9c-9383-07b3dd12cd74",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 3,
                        "zoneId": "Zone.Event.PE.MidgameChallenge.Third.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "86ad5c0f-159d-4b9c-9383-07b3dd12cd74",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 2,
                        "zoneId": "Zone.Event.PE.MidgameChallenge.Fourth.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "86ad5c0f-159d-4b9c-9383-07b3dd12cd74",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    },
                    {
                        "expiresAt": "2099-01-04T00:00:00.000Z",
                        "sortPriority": 1,
                        "zoneId": "Zone.Event.PE.MidgameChallenge.Fifth.Map1",
                        "maxRuns": 1,
                        "resetCostMtx": 0,
                        "eventKey": "86ad5c0f-159d-4b9c-9383-07b3dd12cd74",
                        "flags": [],
                        "dynamicTier": -1,
                        "dynamicGoldTier": -1,
                        "dynamicWorldLevel": -1
                    }
                ],
                "portal_expires": "min",
                "last_forgiven_abandon": "min"
            }
        },
        "commandRevision": 0
    })
    await write_file(f"res/wex/api/game/v2/profile/{account_id}/QueryProfile/monsterpit.json", {
        "_id": await token_generator(),
        "created": await format_time(),
        "updated": await format_time(),
        "rvn": 1,
        "wipeNumber": 4,
        "accountId": account_id,
        "profileId": "monsterpit",
        "version": "remove_pet_upgrades",
        "items": {},
        "stats": {
            "attributes": {
                "highest_pit_power": 0,
                "pit_power_dirty": True,
                "pit_power": 0,
                "pit_level": 1
            }
        },
        "commandRevision": 0
    })
    await write_file(f"res/wex/api/game/v2/profile/{account_id}/QueryProfile/multiplayer.json", {
        "_id": await token_generator(),
        "created": await format_time(),
        "updated": await format_time(),
        "rvn": 1,
        "wipeNumber": 5,
        "accountId": account_id,
        "profileId": "multiplayer",
        "version": "initial",
        "items": {
            str(uuid.uuid4()): {
                "templateId": "MultiplayerMode:PvpDuel",
                "attributes": {
                    "lifetime_wins": 0,
                    "current_enemies_defeated": 0,
                    "defense_rating": 0,
                    "current_losses": 0,
                    "attack_rating": 0,
                    "match_roster": [],
                    "lifetime_enemies_defeated": 0,
                    "recent_matches": [],
                    "pvp_match_count": 0,
                    "match_refresh": {},
                    "current_wins": 0,
                    "recent_opponents": [],
                    "lifetime_losses": 0
                },
                "quantity": 1
            }
        },
        "stats": {
            "attributes": {
                "daily_pvp_wins": 0,
                "last_refresh": "0021-12-01T21:12:00.000Z",
                "current_pvp_win_date": "0021-12-01T21:12:00.000Z",
                "pvp_taunt": "",
                "default_parties": {},
                "matchmaking_id": "",
                "daily_pvp_reward_limit": 25
            }
        },
        "commandRevision": 0
    })
    await write_file(f"res/wex/api/game/v2/profile/{account_id}/QueryProfile/profile0.json", {
        "_id": await token_generator(),
        "created": await format_time(),
        "updated": await format_time(),
        "rvn": 1,
        "wipeNumber": 4,
        "accountId": account_id,
        "profileId": "profile0",
        "version": "initialize_season_end_date",
        "items": {
            str(uuid.uuid4()): {
                "templateId": "HqBuilding:HQ_Market",
                "attributes": {
                    "level": 0
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "Currency:SB_Silver",
                "attributes": {},
                "quantity": 40000
            },
            str(uuid.uuid4()): {
                "templateId": "Energy:PvP",
                "attributes": {
                    "fatigue": 0,
                    "updated": await format_time(),
                    "charge_rate": 1,
                    "max_value": 120
                },
                "quantity": 120
            },
            str(uuid.uuid4()): {
                "templateId": "Currency:SB_WS",
                "attributes": {},
                "quantity": 15000
            },
            str(uuid.uuid4()): {
                "templateId": "HqBuilding:HQ_SpiralTower",
                "attributes": {
                    "level": 0
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "Currency:SB_Bronze",
                "attributes": {},
                "quantity": 80000
            },
            str(uuid.uuid4()): {
                "templateId": "HqBuilding:HQ_HeroTower_Elemental",
                "attributes": {
                    "Normal_static_currency_amount": 100,
                    "Special_static_reward_template_id": "Reagent:Reagent_HeroMap_SuperRare",
                    "level": 0,
                    "chest_options": [
                        {
                            "heroChoicesDeprecated": [],
                            "itemChoices": [
                                "Character:Warrior_Starter_Fire_Berserking_T03",
                                "Character:Warrior_R2_Nature_Whirlwind_T03",
                                "Character:MartialArtist_R2_Water_Ironfist_T03"
                            ],
                            "itemQuantities": [
                                1,
                                1,
                                1
                            ],
                            "heroTrackId": "CoreBasic",
                            "foilLevel": 0
                        }
                    ],
                    "Special_static_currency_template_id": "Reagent:Reagent_HeroMap_Elemental",
                    "Special_static_currency_amount": 500,
                    "Normal_static_reward_amount": 1,
                    "Special_static_reward_amount": 5,
                    "Normal_static_currency_template_id": "Reagent:Reagent_HeroMap_Elemental",
                    "CoreBasic_progress": 0,
                    "chest_info_content_version": "",
                    "page_index": 0,
                    "foil_lvl": -1,
                    "Normal_static_reward_template_id": "Reagent:Reagent_HeroMap_SuperRare"
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "Giftbox:GB_AccountLevel01",
                "attributes": {
                    "sealed_days": 0,
                    "params": {},
                    "min_level": 10
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "Energy:PvE",
                "attributes": {
                    "fatigue": 0,
                    "updated": await format_time(),
                    "charge_rate": 30,
                    "max_value": 300
                },
                "quantity": 300
            },
            str(uuid.uuid4()): {
                "templateId": "HqBuilding:HQ_HeroTower_Bronze",
                "attributes": {
                    "Normal_static_currency_amount": 1,
                    "Normal_static_currency_template_id": "Reagent:Reagent_HeroMap_Bronze",
                    "chest_info_content_version": "",
                    "level": 0,
                    "chest_options": [
                        {
                            "heroChoicesDeprecated": [
                                "Character:Archer_UC1_Fire_ElementalBreath_T03",
                                "Character:MartialArtist_UC1_Nature_ChargedFist_T03",
                                "Character:Knight_UC2_Water_SpearThrust_T03"
                            ],
                            "itemChoices": [],
                            "itemQuantities": [],
                            "heroTrackId": "CoreBronze",
                            "foilLevel": 0
                        }
                    ],
                    "CoreBronze_progress": 0,
                    "page_index": -1,
                    "foil_lvl": -1,
                    "Normal_static_reward_template_id": "",
                    "Normal_static_reward_amount": 1
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "HqBuilding:HQ_PlanarRifts",
                "attributes": {
                    "level": 1
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "MajorEventTracker:MajorEventTracker",
                "attributes": {
                    "level": 0,
                    "seasonId": "0",
                    "totalLevels": 0,
                    "xp": 0,
                    "totalRuns": 0
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "HqBuilding:HQ_CrystalForge",
                "attributes": {
                    "level": 0
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "Currency:SB_Gold",
                "attributes": {},
                "quantity": 25000
            },
            str(uuid.uuid4()): {
                "templateId": "MajorEventTracker:BattlepassSeason",
                "attributes": {
                    "seasonId": "Evergreen5",  # TODO: fetch current bp
                    "level": 0,
                    "totalLevels": 0,
                    "xp": 0,
                    "totalRuns": 0
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "Currency:SB_LevelCompletion",
                "attributes": {},
                "quantity": 125000
            },
            str(uuid.uuid4()): {
                "templateId": "Currency:SB_Mine",
                "attributes": {},
                "quantity": 18000000
            },
            str(uuid.uuid4()): {
                "templateId": "HqBuilding:HQ_HeroTower_SuperRare",
                "attributes": {
                    "Normal_static_currency_amount": 100,
                    "Normal_static_currency_template_id": "Reagent:Reagent_HeroMap_SuperRare",
                    "chest_info_content_version": "",
                    "level": 0,
                    "chest_options": [
                        {
                            "heroChoicesDeprecated": [
                                "Character:Warmage_SR2_Fire_Shadowflame_T05",
                                "Character:MartialArtist_SR1_Dark_ExplodingPalm_T05",
                                "Character:DragonKnight_SR1_Water_JumpStrike_T05"
                            ],
                            "itemChoices": [],
                            "itemQuantities": [],
                            "heroTrackId": "CoreSuperRare",
                            "foilLevel": 0
                        }
                    ],
                    "page_index": -1,
                    "foil_lvl": -1,
                    "Normal_static_reward_template_id": "",
                    "CoreSuperRare_progress": 0,
                    "Normal_static_reward_amount": 1
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "HqBuilding:HQ_AncientFactory",
                "attributes": {
                    "level": 0
                },
                "quantity": 1
            },
            str(uuid.uuid4()): {
                "templateId": "Currency:SB_Platinum",
                "attributes": {},
                "quantity": 15000
            }
        },
        "stats": {
            "attributes": {
                "active_hammer_chest": "",
                "labor_force": {},
                "labor_refill_cd": "min",
                "affiliate_id": "",
                "normalized_name": await normalise_string(display_name),
                "season_xp": 0,
                "mtx_purchase_history": {},
                "default_parties": {},
                "daily_purchases": {},
                "in_app_purchases": {
                    "receipts": [],
                    "packages": []
                },
                "current_battlepass": "Battlepass4",
                "hero_limit": 15,
                "is_pvp_unlocked": False,
                "days_since_started": 0,
                "mtx_level": 0,
                "level": 1,
                "battlepass_purchase_history": {},
                "current_major_event": "",
                "weekly_challenge_xp": 0,
                "starter_hero": "",
                "rep_hero_ids": [],
                "has_started": False,
                "display_name": display_name,
                "secret_shop_page": {
                    "unlock_time": None,
                    "page": 0
                },
                "store_level": 0,
                "market_page": {
                    "unlock_time": None,
                    "page": 0
                },
                "tracked_days_since_started": 0,
                "recent_party_id": "",
                "notification_optin_reward_claimed": False,
                "weapon_limit": 500,
                "starter_hero_template_id": "",
                "vip_level": 0,
                "event_purchases": {
                    "event_id": "",
                    "offers": {}
                },
                "account_perks": {},
                "hero_store_page": {
                    "unlock_time": None,
                    "page": 0
                },
                "activity": {
                    "a": {
                        "date": datetime.datetime.utcnow().strftime("%Y-%m-%dT00:00:00.000Z"),
                        "claimed": False,
                        "props": {
                            "BaseBonus": 10
                        }
                    },
                    "standardGift": 10
                },
                "hammer_quest_energy": {
                    "energy_spent": 0,
                    "energy_required": 100,
                    "claim_count": 0
                },
                "standard_gift": 10,
                "num_territories_claimed": 0,
                "daily_quest_last_refresh": "0021-12-01T21:12:00.000Z",
                "debug_ltm": "",
                "recovery_code": "discord.gg/Mt7SgUu",
                "has_external_account": False,
                "hammer_quest_realtime": {
                    "next_claim": None,
                    "claim_count": 0
                },
                "is_headless": False,
                "current_season_end_date": "2022-12-28T00:00:00.000Z",
                "max_rep_heroes": 1,
                "armor_limit": 500,
                "season_regular_claim_level": -1,
                "rewards_claimed": {},
                "last_reported_account_level_milestone": 0,
                "rocket_unlock": 0,
                "last_battlepass_purchased": "",
                "inventory_limit_bonus": 0,
                "weekly_purchases": {},
                "num_levels_completed": 0,
                "avatar_url": "wex-temp-avatar.png",
                "weekly_challenge_level": 0,
                "monthly_purchases": {},
                "xp": 0,
                "event_next_level": 0,
                "login_reward": {
                    "last_claim_time": "0021-12-01T21:12:00.000Z",
                    "next_level": 1
                },
                "season_premium_claim_level": -1,
                "come_back_reward_claimed": False,
                "is_developer": False
            }
        },
        "commandRevision": 2
    })
    await write_file(f"res/wex/api/receipts/v1/account/{account_id}.json", [])
    return account_id
