"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Class based system to handle the profile management for wex mcp service
"""
import ast
import asyncio
import uuid
import enum
from concurrent.futures.thread import ThreadPoolExecutor

import aiofiles
import orjson
import sanic


class ProfileType(enum.Enum):
    """
    Enum for the profile types
    """
    PROFILE0 = "profile0"
    LEVELS = "levels"
    FRIENDS = "friends"
    MONSTERPIT = "monsterpit"
    MULTIPLAYER = "multiplayer"

    @classmethod
    def from_string(cls, s: str) -> "ProfileType":
        """
        Get the profile ID from the string
        :param s: The string to get the profile ID from
        :return: The profile ID
        """
        try:
            return cls[s.upper()]
        except KeyError:
            raise sanic.exceptions.BadRequest(f"{s} is not a valid profile")


class PlayerProfile:
    """
    Class based system to handle the profile management for wex mcp service
    """

    def __init__(self, account_id: str) -> None:
        """
        Initialise the profile.
        This will load the profile from the res folder and setup the variables
        :param account_id: The account ID of the profile
        """
        self.account_id = account_id
        self.friends = None
        self.friends_changes = []
        self.friends_notifications = []
        self.levels = None
        self.levels_changes = []
        self.levels_notifications = []
        self.monsterpit = None
        self.monsterpit_changes = []
        self.monsterpit_notifications = []
        self.multiplayer = None
        self.multiplayer_changes = []
        self.multiplayer_notifications = []
        self.profile0 = None
        self.profile0_changes = []
        self.profile0_notifications = []
        self.profile_revisions = None
        try:
            asyncio.get_running_loop()
            with ThreadPoolExecutor() as pool:
                pool.submit(lambda: asyncio.run(self.load_profile())).result()
        except RuntimeError:
            asyncio.run(self.load_profile())

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

    async def load_profile(self) -> None:
        """
        Load the profile based on the account ID and setup the variables
        :return: None
        """
        for filename in ProfileType:
            async with aiofiles.open(
                    f"res/wex/api/game/v2/profile/{self.account_id}/QueryProfile/{filename.value}.json", "rb") as file:
                profile = orjson.loads(await file.read())
            # Migrate the profile to the correct format
            if profile.get("profileChanges") is not None:
                profile = profile["profileChanges"][0]["profile"]
                async with aiofiles.open(
                        f"res/wex/api/game/v2/profile/{self.account_id}/QueryProfile/{filename.value}.json",
                        "wb") as file:
                    await file.write(orjson.dumps(profile))
            setattr(self, filename.value, profile)
        self.profile_revisions = [
            {"profileId": "profile0", "clientCommandRevision": self.profile0["commandRevision"]},
            {"profileId": "levels", "clientCommandRevision": self.levels["commandRevision"]},
            {"profileId": "friends", "clientCommandRevision": self.friends["commandRevision"]},
            {"profileId": "monsterpit", "clientCommandRevision": self.monsterpit["commandRevision"]},
            {"profileId": "multiplayer", "clientCommandRevision": self.multiplayer["commandRevision"]}]

    async def get_profile(self, profile_id: ProfileType = ProfileType.PROFILE0) -> dict:
        """
        Get the profile data
        :param profile_id: The profile ID to get
        :return: The profile data
        """
        return getattr(self, profile_id.value)

    async def get_item_by_guid(self, guid: str, profile_id: ProfileType = ProfileType.PROFILE0) -> dict:
        """
        Get the item by the GUID
        :param profile_id: The profile ID to get
        :param guid: The GUID of the item
        :return: The item
        """
        if isinstance(guid, list):
            guid = guid[0]
        return (await self.get_profile(profile_id)).get("items").get(guid)

    async def find_item_by_template_id(self, template_id: str, profile_id: ProfileType = ProfileType.PROFILE0) -> list:
        """
        Find all items with the specified template ID
        :param template_id: The template ID to search for
        :param profile_id: The profile ID to get
        :return: A list of GUIDs of the items with the specified template ID
        """
        guids = []
        for guid, item in (await self.get_profile(profile_id)).get("items").items():
            if item["templateId"] == template_id:
                guids.append(guid)
        return guids

    async def fuzzy_find_item_by_template_id(self, template_id: str,
                                             profile_id: ProfileType = ProfileType.PROFILE0) -> list:
        """
        Find all items with the specified template ID. Not actually fuzzy search, just searches for tID after :
        :param template_id: The template ID to search for
        :param profile_id: The profile ID to get
        :return: A list of GUIDs of the items with the specified template ID
        """
        guids = []
        for guid, item in (await self.get_profile(profile_id)).get("items").items():
            if item["templateId"].split(":")[-1] == template_id:
                guids.append(guid)
        return guids

    async def find_items_by_type(self, template_id: str, profile_id: ProfileType = ProfileType.PROFILE0) -> list:
        """
        Find all items with the specified type.
        :param template_id: The template ID to search for
        :param profile_id: The profile ID to get
        :return: A list of GUIDs of the items with the specified template ID
        """
        guids = []
        for guid, item in (await self.get_profile(profile_id)).get("items").items():
            if item["templateId"].split(":")[0] == template_id:
                guids.append(guid)
        return guids

    async def get_stat(self, stat_name: str,
                       profile_id: ProfileType = ProfileType.PROFILE0) -> str | int | float | dict | list:
        """
        Get the specified stat from the profile
        :param stat_name: The name of the stat to get
        :param profile_id: The profile ID to get
        :return: The value of the stat
        """
        return (await self.get_profile(profile_id)).get("stats").get("attributes").get(stat_name)

    async def modify_stat(self, stat_name: str, new_value: str | int | dict | list | float,
                          profile_id: ProfileType = ProfileType.PROFILE0) -> None:
        """
        Modify the specified stat to the new value
        :param stat_name: The name of the stat to modify
        :param new_value: The new value of the stat
        :param profile_id: The ID of the profile to modify
        :raise AttributeError: If the profile ID is invalid
        :return: None
        """
        profile_changes = getattr(self, f"{profile_id.value}_changes", [])
        profile_changes.append({"changeType": "statModified", "name": stat_name, "value": new_value})
        setattr(self, f"{profile_id.value}_changes", profile_changes)

    async def remove_item(self, item_id: str, profile_id: ProfileType = ProfileType.PROFILE0) -> None:
        """
        Remove the specified item from the profile
        :param item_id: The GUID of the item to remove
        :param profile_id: The ID of the profile to modify
        :raise AttributeError: If the profile ID is invalid
        :return: None
        """
        profile_changes = getattr(self, f"{profile_id.value}_changes", [])
        profile_changes.append({"changeType": "itemRemoved", "itemId": item_id})
        setattr(self, f"{profile_id.value}_changes", profile_changes)

    async def change_item_attribute(self, item_id: str, attribute_name: str, new_value: str | int | dict | list | float,
                                    profile_id: ProfileType = ProfileType.PROFILE0) -> None:
        """
        Change the specified attribute of the specified item to the new value
        :param item_id: The GUID of the item to modify
        :param attribute_name: The name of the attribute to modify
        :param new_value: The new value of the attribute
        :param profile_id: The ID of the profile to modify
        :raise AttributeError: If the profile ID is invalid
        :return: None
        """
        profile_changes = getattr(self, f"{profile_id.value}_changes", [])
        profile_changes.append({"changeType": "itemAttrChanged", "itemId": item_id, "attributeName": attribute_name,
                                "attributeValue": new_value})
        setattr(self, f"{profile_id.value}_changes", profile_changes)

    async def add_item(self, item_data: dict, item_id: str | None = None,
                       profile_id: ProfileType = ProfileType.PROFILE0) -> str:
        """
        Add the specified item to the profile
        :param item_data: The data of the item to add
        :param item_id: The GUID of the item to add
        :param profile_id: The ID of the profile to modify
        :raise AttributeError: If the profile ID is invalid
        :return: None
        """
        if item_id is None:
            item_id = str(uuid.uuid4())
        profile_changes = getattr(self, f"{profile_id.value}_changes", [])
        profile_changes.append({"changeType": "itemAdded", "itemId": item_id, "item": item_data})
        setattr(self, f"{profile_id.value}_changes", profile_changes)
        return item_id

    async def change_item_quantity(self, item_id: str, new_quantity: int | float,
                                   profile_id: ProfileType = ProfileType.PROFILE0) -> None:
        """
        Change the quantity of the specified item to the new value
        :param item_id: The GUID of the item to modify
        :param new_quantity: The new quantity of the item
        :param profile_id: The ID of the profile to modify
        :raise AttributeError: If the profile ID is invalid
        :return: None
        """
        profile_changes = getattr(self, f"{profile_id.value}_changes", [])
        profile_changes.append({"changeType": "itemQuantityChanged", "itemId": item_id, "quantity": new_quantity})
        setattr(self, f"{profile_id.value}_changes", profile_changes)

    async def get_notifications(self, profile_id: ProfileType = ProfileType.PROFILE0) -> list[dict]:
        """
        Get the notifications for the current account and profile
        :param profile_id: The ID of the profile to get
        :return: The notifications
        """
        return getattr(self, f"{profile_id.value}_notifications", [])

    async def add_notifications(self, notification: dict, profile_id: ProfileType = ProfileType.PROFILE0) -> list[dict]:
        """
        Adds notifications for the current account and profile
        :param notification: The notification to add to
        :param profile_id: The ID of the profile to add to
        :return: The notifications
        """
        profile_notifications = getattr(self, f"{profile_id.value}_notifications", [])
        profile_notifications.append(notification)
        setattr(self, f"{profile_id.value}_notifications", profile_notifications)
        return profile_notifications

    async def clear_notifications(self, profile_id: ProfileType | None = None) -> None:
        """
        Clears notifications for the current account and profile
        :param profile_id: The ID of the profile to clear
        :return: The notifications
        """
        profile_types = ProfileType if profile_id is None else [profile_id]

        for p_type in profile_types:
            setattr(self, f"{p_type.value}_notifications", [])

    async def flush_changes(self, profile_type: ProfileType | None = None) -> None:
        """
        Apply all changes to the original profiles.

        :param profile_type: (Optional) Enum of the profile to flush. If None, all profiles will be flushed.
        """
        profile_types = ProfileType if profile_type is None else [profile_type]

        for p_type in profile_types:
            profile = await self.get_profile(p_type)
            for change in getattr(self, f"{p_type.value}_changes"):
                change_type = change["changeType"]
                if change_type == "statModified":
                    profile["stats"]["attributes"][change["name"]] = change["value"]
                elif change_type == "itemRemoved":
                    del profile["items"][change["itemId"]]
                elif change_type == "itemAttrChanged":
                    profile["items"][change["itemId"]]["attributes"][change["attributeName"]] = change["attributeValue"]
                elif change_type == "itemAdded":
                    profile["items"][change["itemId"]] = change["item"]
                elif change_type == "itemQuantityChanged":
                    profile["items"][change["itemId"]]["quantity"] = change["quantity"]
            setattr(self, f"{p_type.value}", profile)

            # Clear the changes list for this profile
            setattr(self, f"{p_type.value}_changes", [])

    async def construct_response(self, profile_id: ProfileType = ProfileType.PROFILE0, rvn: int = -1,
                                 client_command_revision: str | None = None, clear_notification: bool = False) -> dict:
        """
        Construct a response for the specified profile
        :param profile_id: The profile to construct a response for
        :param rvn: The revision number of the profile
        :param client_command_revision: The revision number of the client command
        :param clear_notification: Whether to clear the notifications after constructing the response
        :return: The response
        """
        from utils.utils import format_time
        if client_command_revision is None:
            client_command_revision = self.profile_revisions
        else:
            client_command_revision = ast.literal_eval(client_command_revision)
        for item in client_command_revision:
            if item["profileId"] == profile_id.value:
                client_revision = item["clientCommandRevision"]
                break
        else:
            client_revision = -1
        if client_revision <= 0:
            client_revision = (await self.get_profile(profile_id))["commandRevision"]
        response = {
            "profileRevision": (await self.get_profile(profile_id))["rvn"],
            "profileId": profile_id.value,
            "profileChangesBaseRevision": (await self.get_profile(profile_id))["rvn"],
            "profileChanges": [],
            "profileCommandRevision": client_revision,
            "serverTime": await format_time(),
            "responseVersion": 1
        }

        if rvn != (await self.get_profile(profile_id))["rvn"]:
            # Full profile update requested
            await self.flush_changes(profile_id)
            response['profileChanges'] = [
                {
                    "changeType": "fullProfileUpdate",
                    "profile": await self.get_profile(profile_id)
                }
            ]
        else:
            # Partial profile update requested
            profile_changes = getattr(self, f"{profile_id.value}_changes", [])
            if profile_changes:
                response['profileChanges'] = profile_changes
                await self.bump_revision(profile_id, response)

        # Check for other profiles with changes
        other_changes = []
        for profile in ProfileType:
            if profile == profile_id:
                continue
            profile_changes = getattr(self, f"{profile.value}_changes", [])
            if profile_changes:
                profile_notifications = getattr(self, f"{profile.value}_notifications", [])
                for item in client_command_revision:
                    if item["profileId"] == profile.value:
                        client_revision = item["clientCommandRevision"]
                        break
                else:
                    client_revision = -1
                if client_revision <= 0:
                    client_revision = (await self.get_profile(profile))["commandRevision"]
                base_rvn = (await self.get_profile(profile))["rvn"]
                await self.bump_revision(profile)
                other_changes.append({
                    "profileRevision": (await self.get_profile(profile))["rvn"],
                    "profileId": profile.value,
                    "profileChangesBaseRevision": base_rvn,
                    "profileChanges": profile_changes,
                    "profileCommandRevision": client_revision,
                })
                if profile_notifications:
                    other_changes[-1]["notifications"] = profile_notifications

        if other_changes:
            response['multiUpdate'] = other_changes
        notifications = getattr(self, f"{profile_id.value}_notifications", [])
        if notifications:
            response["notifications"] = notifications

        if clear_notification:
            await self.clear_notifications(profile_id)

        await self.flush_changes()
        await self.save_profile()

        return response

    async def bump_revision(self, profile_id: ProfileType = ProfileType.PROFILE0, response: dict | None = None) -> None:
        """
        Bump the revision of the specified profile
        :param profile_id: The profile to bump the revision of
        :param response: The response to add the revision to
        :return: None
        """
        from utils.utils import format_time
        (await self.get_profile(profile_id))["rvn"] += 1
        (await self.get_profile(profile_id))["updated"] = await format_time()
        (await self.get_profile(profile_id))["commandRevision"] += 1
        if response is not None:
            response["profileRevision"] = (await self.get_profile(profile_id))["rvn"]
            response["profileChangesBaseRevision"] = (await self.get_profile(profile_id))["rvn"] - 1
            response["profileCommandRevision"] = (await self.get_profile(profile_id))["commandRevision"]
        for i, client_revision in enumerate(self.profile_revisions):
            if client_revision["profileId"] == profile_id.value:
                self.profile_revisions[i]["clientCommandRevision"] += 1
                break

    async def save_profile(self) -> None:
        """
        Save the modified profiles to disk
        :return: None
        """
        save_profile = False
        if save_profile:
            for profile_type in ProfileType:
                profile = await self.get_profile(profile_type)
                async with aiofiles.open(
                        f"res/wex/api/game/v2/profile/{self.account_id}/QueryProfile/{profile_type.value}.json",
                        "wb") as file:
                    await file.write(orjson.dumps(profile))
