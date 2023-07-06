"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Handles the enums
"""

import enum

from utils.exceptions import errors


class ProfileType(enum.Enum):
    """
    Enum for the profile types

    Attributes:
        PROFILE0: The profile ID for the profile0 profile
        LEVELS: The profile ID for the levels profile
        FRIENDS: The profile ID for the friends profile
        MONSTERPIT: The profile ID for the monsterpit profile
        MULTIPLAYER: The profile ID for the multiplayer profile

    Methods:
        from_string(cls, s: str) -> "ProfileType":
            Get the profile ID from the string
    """
    PROFILE0: str = "profile0"
    LEVELS: str = "levels"
    FRIENDS: str = "friends"
    MONSTERPIT: str = "monsterpit"
    MULTIPLAYER: str = "multiplayer"

    @classmethod
    def from_string(cls, s: str) -> "ProfileType":
        """
        Get the profile ID from the string
        :param s: The string to get the profile ID from
        :return: The profile ID
        :raises: errors.com.epicgames.modules.profile.invalid_profile_id_param: Raised if the profile ID is invalid
        """
        try:
            return cls[s.upper()]
        except KeyError:
            raise errors.com.epicgames.modules.profile.invalid_profile_id_param()


class FriendStatus(enum.Enum):
    """
    Enum for the different friend statuses in a WEX Profile

    Attributes:
        NONE: No friend status
        SUGGESTED: Suggested friend
        REQUESTED: Outgoing friend request
        INVITED: Incoming friend request
        FRIEND: Normal friend
        EPICFRIEND: Epic friend (1.80+)
        EPICNONPLATFORMFRIEND: Epic friend on a different platform
        PLATFORMONLYFRIEND: Friend on a different platform
        SUGGESTEDREQUEST: Suggested friend request sent
        SUGGESTEDLEGACY: Suggested friend from legacy
        NOTPLAYING: Not playing
        PLATFORMNOTPLAYING: Not playing on a different platform
        MAXNONE: Max friends reached

    Methods:
        from_string(cls, s: str) -> "FriendStatus":
            Get the friend status from a string
    """
    NONE: str = "None"
    SUGGESTED: str = "Suggested"
    REQUESTED: str = "Requested"
    INVITED: str = "Invited"
    FRIEND: str = "Friend"
    EPICFRIEND: str = "EpicFriend"
    EPICNONPLATFORMFRIEND: str = "EpicNonPlatformFriend"
    PLATFORMONLYFRIEND: str = "PlatformOnlyFriend"
    SUGGESTEDREQUEST: str = "SuggestedRequest"
    SUGGESTEDLEGACY: str = "SuggestedLegacy"
    NOTPLAYING: str = "NotPlaying"
    PLATFORMNOTPLAYING: str = "PlatformNotPlaying"
    MAXNONE: str = "Max_None"

    @classmethod
    def from_string(cls, s: str) -> "FriendStatus":
        """
        Get the friend status from a string
        :param s: The string to get the friend status from
        :return: The friend status
        """
        return cls[s.upper()]
