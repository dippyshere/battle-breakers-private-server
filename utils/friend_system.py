"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Class based system to handle the friends service management
"""
import asyncio
import datetime
import os
import random
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Optional

import aiofiles
import orjson
import sanic

from utils.exceptions import errors
from utils.profile_system import PlayerProfile, ProfileType
from utils.utils import format_time


class PlayerFriends:
    """
    Class based system to handle the friends service management
    """

    def __init__(self, account_id: str) -> None:
        """
        Initialise the friends class.
        This will load the profile from the res folder and setup the variables
        :param account_id: The account ID of the profile
        """
        self.account_id: str = account_id
        self.friends: Optional[dict] = None
        try:
            asyncio.get_running_loop()
            with ThreadPoolExecutor() as pool:
                pool.submit(lambda: asyncio.run(self.load_friends())).result()
        except RuntimeError:
            asyncio.run(self.load_friends())

    def __str__(self) -> str:
        """
        Return the account ID of the profile
        :return: The account ID of the profile
        """
        return self.account_id

    def __repr__(self) -> str:
        """
        Return the account ID of the profile
        :return: The account ID of the profile
        """
        return self.account_id

    async def load_friends(self) -> None:
        """
        Load the profile based on the account ID and setup the variables
        :return: None
        """
        async with aiofiles.open(f"res/friends/api/v1/{self.account_id}.json", "rb") as file:
            self.friends: dict = orjson.loads(await file.read())

    async def get_friends(self) -> dict:
        """
        Get the friends data
        :return: The friend data
        """
        return self.friends

    async def get_summary(self) -> dict:
        """
        Get the friends data summary
        :return: The friend data
        """
        # TODO: mutuals calculation if bothered
        return self.friends

    async def get_legacy_summary(self) -> list[dict]:
        """
        Get the legacy friends data for old clients
        :return: The friend data
        """
        friends: list = []
        for friend in self.friends["friends"]:
            friends.append({
                "accountId": friend["accountId"],
                "status": "ACCEPTED",
                "direction": friend.get("direction", "INBOUND"),
                "created": friend["created"],
                "favorite": friend["favorite"]
            })
        for friend in self.friends["incoming"]:
            friends.append({
                "accountId": friend["accountId"],
                "status": "PENDING",
                "direction": "INBOUND",
                "created": friend["created"],
                "favorite": False
            })
        for friend in self.friends["outgoing"]:
            friends.append({
                "accountId": friend["accountId"],
                "status": "PENDING",
                "direction": "OUTBOUND",
                "created": friend["created"],
                "favorite": False
            })
        return friends

    async def send_friend_request(self, request: sanic.request.Request, friendId: str) -> None | dict:
        """
        Send a friend request to a player
        :param request: The request object
        :param friendId: The account ID of the player to send the request to
        :return: The response of the request
        """
        for friend in self.friends["friends"]:
            if friend["accountId"] == friendId:
                raise errors.com.epicgames.friends.duplicate_friendship()
        for friend in self.friends["outgoing"]:
            if friend["accountId"] == friendId:
                raise errors.com.epicgames.friends.friend_request_already_sent()
        if friendId not in request.app.ctx.friends:
            request.app.ctx.friends[friendId]: PlayerFriends = PlayerFriends(friendId)
        other_friend: PlayerFriends = request.app.ctx.friends[friendId]
        for friend in self.friends["incoming"]:
            if friend["accountId"] == friendId:
                await other_friend.add_friend(self.account_id)
                await self.add_friend(friendId)
                return
        if other_friend.friends["settings"]["acceptInvites"] != "public":
            raise errors.com.epicgames.friends.cannot_friend_due_to_target_settings()
        for blocked in other_friend.friends["blocklist"]:
            if blocked["accountId"] == self.account_id:
                raise errors.com.epicgames.friends.cannot_friend_due_to_target_settings()
        if friendId not in request.app.ctx.profiles:
            request.app.ctx.profiles[friendId]: PlayerProfile = PlayerProfile(friendId)
        wex_data: dict = await request.app.ctx.profiles[friendId].get_profile(ProfileType.PROFILE0)
        rep_heroes: list = []
        account_perks: list = []
        account_data: dict = await request.app.ctx.read_file(f"res/account/api/public/account/{friendId}.json")
        for account_perk in ["MaxHitPoints", "RegenStat", "PetStrength", "BasicAttack", "Attack", "SpecialAttack",
                             "DamageReduction", "MaxMana"]:
            account_perks.append(wex_data["stats"]["attributes"].get("account_perks").get(account_perk, 0))
        for hero_id in wex_data["stats"]["attributes"].get("rep_hero_ids", []):
            hero_data: dict = await request.app.ctx.profiles[friendId].get_item_by_guid(hero_id)
            rep_heroes.append({
                "itemId": hero_id,
                "templateId": hero_data.get("templateId"),
                "bIsCommander": True,
                "level": hero_data.get("attributes").get("level"),
                "skillLevel": hero_data.get("attributes").get("skill_level"),
                "upgrades": hero_data.get("attributes").get("upgrades"),
                "accountInfo": {
                    "level": wex_data["stats"]["attributes"].get("level", 0),
                    "perks": account_perks
                },
                "foilLevel": hero_data.get("attributes").get("foil_lvl", -1),
                "gearTemplateId": hero_data.get("attributes").get("sidekick_template_id", ""),
            })
        await request.app.ctx.profiles[self.account_id].add_item({
            "templateId": "Friend:Instance",
            "attributes": {
                "lifetime_claimed": 0,
                "accountId": account_data["id"],
                "canBeSparred": False,
                "snapshot_expires": await request.app.ctx.format_time(
                    datetime.datetime.utcnow() + datetime.timedelta(hours=3)),
                "best_gift": 0,  # These stats are unique to the friend instance on the profile, not the friend
                "lifetime_gifted": 0,
                "snapshot": {
                    "displayName": account_data["displayName"],
                    "avatarUrl": "wex-temp-avatar.png",
                    "repHeroes": rep_heroes,
                    "lastPlayTime": wex_data["updated"],
                    "numLevelsCompleted": wex_data["stats"]["attributes"].get("num_levels_completed", 0),
                    "numTerritoriesClaimed": wex_data["stats"]["attributes"].get("num_territories_claimed", 0),
                    "accountLevel": wex_data["stats"]["attributes"].get("level", 0),
                    "numRepHeroes": len(wex_data["stats"]["attributes"].get("rep_hero_ids", [])),
                    "isPvPUnlocked": wex_data["stats"]["attributes"].get("is_pvp_unlocked", False)
                },
                "remoteFriendId": "",
                "status": "Requested",
                "gifts": {}
            },
            "quantity": 1
        }, profile_id=ProfileType.FRIENDS)
        self.friends["outgoing"].append({
            "accountId": friendId,
            "mutual": 0,
            "favorite": False,
            "created": await format_time()
        })
        await self.save_friends()
        if self.account_id not in request.app.ctx.profiles:
            request.app.ctx.profiles[self.account_id]: PlayerProfile = PlayerProfile(self.account_id)
        wex_data: dict = await request.app.ctx.profiles[self.account_id].get_profile(ProfileType.PROFILE0)
        rep_heroes: list = []
        account_perks: list = []
        account_data: dict = await request.app.ctx.read_file(
            f"res/account/api/public/account/{self.account_id}.json")
        for account_perk in ["MaxHitPoints", "RegenStat", "PetStrength", "BasicAttack", "Attack", "SpecialAttack",
                             "DamageReduction", "MaxMana"]:
            account_perks.append(wex_data["stats"]["attributes"].get("account_perks").get(account_perk, 0))
        for hero_id in wex_data["stats"]["attributes"].get("rep_hero_ids", []):
            hero_data: dict = await request.app.ctx.profiles[self.account_id].get_item_by_guid(hero_id)
            rep_heroes.append({
                "itemId": hero_id,
                "templateId": hero_data.get("templateId"),
                "bIsCommander": True,
                "level": hero_data.get("attributes").get("level"),
                "skillLevel": hero_data.get("attributes").get("skill_level"),
                "upgrades": hero_data.get("attributes").get("upgrades"),
                "accountInfo": {
                    "level": wex_data["stats"]["attributes"].get("level", 0),
                    "perks": account_perks
                },
                "foilLevel": hero_data.get("attributes").get("foil_lvl", -1),
                "gearTemplateId": hero_data.get("attributes").get("sidekick_template_id", ""),
            })
        await request.app.ctx.profiles[friendId].add_item({
            "templateId": "Friend:Instance",
            "attributes": {
                "lifetime_claimed": 0,
                "accountId": account_data["id"],
                "canBeSparred": False,
                "snapshot_expires": await request.app.ctx.format_time(
                    datetime.datetime.utcnow() + datetime.timedelta(hours=3)),
                "best_gift": 0,  # These stats are unique to the friend instance on the profile, not the friend
                "lifetime_gifted": 0,
                "snapshot": {
                    "displayName": account_data["displayName"],
                    "avatarUrl": "wex-temp-avatar.png",
                    "repHeroes": rep_heroes,
                    "lastPlayTime": wex_data["updated"],
                    "numLevelsCompleted": wex_data["stats"]["attributes"].get("num_levels_completed", 0),
                    "numTerritoriesClaimed": wex_data["stats"]["attributes"].get("num_territories_claimed", 0),
                    "accountLevel": wex_data["stats"]["attributes"].get("level", 0),
                    "numRepHeroes": len(wex_data["stats"]["attributes"].get("rep_hero_ids", [])),
                    "isPvPUnlocked": wex_data["stats"]["attributes"].get("is_pvp_unlocked", False)
                },
                "remoteFriendId": "",
                "status": "Invited",
                "gifts": {}
            },
            "quantity": 1
        }, profile_id=ProfileType.FRIENDS)
        other_friend.friends["incoming"].append({
            "accountId": self.account_id,
            "mutual": 0,
            "favorite": False,
            "created": await format_time()
        })
        await other_friend.save_friends()

    async def add_friend(self, friendId: str) -> None:
        """
        Add a friend to the profile
        :param friendId: The account ID of the player to add
        :return: None
        """
        for friend in self.friends["friends"]:
            if friend["accountId"] == friendId:
                return
        for friend in self.friends["incoming"]:
            if friend["accountId"] == friendId:
                self.friends["friends"].append({
                    "accountId": friendId,
                    "groups": [],
                    "mutual": 0,
                    "alias": "",
                    "note": "",
                    "favorite": False,
                    "created": await format_time(),
                    "direction": "INBOUND"
                })
                self.friends["incoming"].remove(friend)
                await self.save_friends()
                return
        for friend in self.friends["outgoing"]:
            if friend["accountId"] == friendId:
                self.friends["friends"].append({
                    "accountId": friendId,
                    "groups": [],
                    "mutual": 0,
                    "alias": "",
                    "note": "",
                    "favorite": False,
                    "created": await format_time(),
                    "direction": "OUTBOUND"
                })
                self.friends["outgoing"].remove(friend)
                await self.save_friends()
                return
        self.friends["friends"].append({
            "accountId": friendId,
            "groups": [],
            "mutual": 0,
            "alias": "",
            "note": "",
            "favorite": False,
            "created": await format_time(),
            "direction": "INBOUND"
        })
        await self.save_friends()

    async def remove_friend(self, request: sanic.request.Request, friendId: str) -> None:
        """
        Cancel/decline a friend request / remove a friend
        :param request: The request object
        :param friendId: The account ID of the player to cancel the request to
        :return: The response of the request
        """
        for friend in self.friends["friends"]:
            if friend["accountId"] == friendId:
                self.friends["friends"].remove(friend)
                break
        for friend in self.friends["incoming"]:
            if friend["accountId"] == friendId:
                self.friends["incoming"].remove(friend)
                break
        for friend in self.friends["outgoing"]:
            if friend["accountId"] == friendId:
                self.friends["outgoing"].remove(friend)
                break
        await self.save_friends()
        try:
            if friendId not in request.app.ctx.friends:
                request.app.ctx.friends[friendId]: PlayerFriends = PlayerFriends(friendId)
            other_friend: PlayerFriends = request.app.ctx.friends[friendId]
            for friend in other_friend.friends["friends"]:
                if friend["accountId"] == self.account_id:
                    other_friend.friends["friends"].remove(friend)
                    break
            for friend in other_friend.friends["incoming"]:
                if friend["accountId"] == self.account_id:
                    other_friend.friends["incoming"].remove(friend)
                    break
            for friend in other_friend.friends["outgoing"]:
                if friend["accountId"] == self.account_id:
                    other_friend.friends["outgoing"].remove(friend)
                    break
            await other_friend.save_friends()
        except:
            pass

    async def update_friends(self, friends: dict) -> None:
        """
        Update the friends data
        :param friends: The new friends data
        :return: None
        """
        self.friends: dict = friends
        await self.save_friends()

    async def save_friends(self) -> None:
        """
        Save the new friends data to the res folder
        :return: None
        """
        save_friends: bool = False
        if save_friends:
            async with aiofiles.open(f"res/friends/api/v1/{self.account_id}.json", "wb") as file:
                await file.write(orjson.dumps(self.friends))

    async def suggest_friends(self, request: sanic.request.Request) -> list[str]:
        """
        Suggest friends for the player
        :param request: The request object
        :return: The response of the request
        """
        suggested_accounts: list[str] = []
        accounts_list: list[str] = os.listdir("res/account/api/public/account")
        accounts_list: list[str] = [account.split(".")[0] for account in accounts_list]
        # This just forces this account to be the first suggestion :)
        if "ec0ebb7e56f6454e86c62299a7b32e20" in accounts_list:
            accounts_list.remove("ec0ebb7e56f6454e86c62299a7b32e20")
        accounts_list.insert(0, "ec0ebb7e56f6454e86c62299a7b32e20")
        if self.account_id in accounts_list:
            accounts_list.remove(self.account_id)
        for account in accounts_list:
            if account not in request.app.ctx.friends:
                request.app.ctx.friends[account]: PlayerFriends = PlayerFriends(account)
            if request.app.ctx.friends[account].friends["settings"]["acceptInvites"] != "public":
                accounts_list.remove(account)
        for _ in range(10):
            if len(accounts_list) == 0:
                break
            suggested_accounts.append(random.choice(accounts_list))
            accounts_list.remove(suggested_accounts[-1])
        self.friends["suggested"] = []
        for suggestion in suggested_accounts:
            self.friends["suggested"].append({
                "accountId": suggestion,
                "mutual": 0,
            })
        await self.save_friends()
        return suggested_accounts
