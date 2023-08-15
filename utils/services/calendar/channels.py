"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Class based systems for each of the channels in the calendar service
"""
from typing import Any

from utils.profile_system import MCPTypes


class State:
    """
    Class based system to handle states of a channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the states class.
        This will setup the variables for the state
        """
        self.validFrom: str = ""
        self.activeEvents: list[str] = []
        self.state: dict[str, MCPTypes] = {}

    def __repr__(self) -> str:
        """
        Get the representation of the state class
        :return: The representation of the state class
        """
        return f"<State>"

    def __str__(self) -> str:
        """
        Get the string of the state class
        :return: The string of the state class
        """
        return self.__repr__()

    def __dict__(self) -> dict[str, Any]:
        """
        Get the dictionary of the state class
        :return: The dictionary of the state class
        """
        return {
            "validFrom": self.validFrom,
            "activeEvents": self.activeEvents,
            "state": self.state
        }

    def __getitem__(self, key: str) -> Any:
        """
        Get the value of the key in the state class
        :param key: The key to get the value of
        :return: The value of the key in the state class
        """
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value of the key in the state class
        :param key: The key to set the value of
        :param value: The value to set the key to
        :return: The value of the key in the state class
        """
        setattr(self, key, value)

    def __delitem__(self, key: str) -> None:
        """
        Delete the key in the state class
        :param key: The key to delete
        :return: The value of the key in the state class
        """
        delattr(self, key)

    def __len__(self) -> int:
        """
        Get the length of the state
        :return: The length of the state
        """
        return len(self.__dict__())


class Channel:
    """
    Class based system to handle a channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the channel class.
        This will setup the variables for the channel
        """
        self.states: dict[str, State] = {}
        self.cacheExpire: str = ""

    def __repr__(self) -> str:
        """
        Get the representation of the channel class
        :return: The representation of the channel class
        """
        return f"<Channel>"

    def __str__(self) -> str:
        """
        Get the string of the channel class
        :return: The string of the channel class
        """
        return self.__repr__()

    def __dict__(self) -> dict[str, Any]:
        """
        Get the dictionary of the channel class
        :return: The dictionary of the channel class
        """
        return {
            "states": self.states,
            "cacheExpire": self.cacheExpire
        }

    def __getitem__(self, key: str) -> Any:
        """
        Get the value of the key in the channel class
        :param key: The key to get the value of
        :return: The value of the key in the channel class
        """
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value of the key in the channel class
        :param key: The key to set the value of
        :param value: The value to set the key to
        :return: The value of the key in the channel class
        """
        setattr(self, key, value)

    def __delitem__(self, key: str) -> None:
        """
        Delete the key in the channel class
        :param key: The key to delete
        :return: The value of the key in the channel class
        """
        delattr(self, key)

    def __len__(self) -> int:
        """
        Get the length of the channel
        :return: The length of the channel
        """
        return len(self.__dict__())


class News(Channel):
    """
    Class based system to handle the news channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the news channel class.
        This will setup the variables for the news channel
        """
        super().__init__()

    def update_events(self) -> None:
        """
        Update the events for the news channel
        :return: None
        """
        pass


class LimitedTimeMode(Channel):
    """
    Class based system to handle the limited time mode channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the limited time mode channel class.
        This will setup the variables for the limited time mode channel
        """
        super().__init__()

    def update_events(self) -> None:
        """
        Update the events for the limited time mode channel
        :return:
        """
        pass


class Marketing(Channel):
    """
    Class based system to handle the marketing channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the marketing channel class.
        This will setup the variables for the marketing channel
        """
        super().__init__()

    def update_events(self) -> None:
        """
        Update the events for the marketing channel
        :return:
        """
        pass


class RotationalContent(Channel):
    """
    Class based system to handle the rotational content channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the rotational content channel class.
        This will setup the variables for the rotational content channel
        """
        super().__init__()

    def update_events(self) -> None:
        """
        Update the events for the rotational content channel
        :return:
        """
        pass


class FeaturedStoresMcp(Channel):
    """
    Class based system to handle the featured stores mcp channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the featured stores mcp channel class.
        This will setup the variables for the featured stores mcp channel
        """
        super().__init__()

    def update_events(self) -> None:
        """
        Update the events for the featured stores mcp channel
        :return:
        """
        pass


class WeeklyChallenge(Channel):
    """
    Class based system to handle the weekly challenge mcp channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the weekly challenge mcp channel class.
        This will setup the variables for the weekly challenge mcp channel
        """
        super().__init__()

    def update_events(self) -> None:
        """
        Update the events for the weekly challenge channel
        :return:
        """
        pass


class BattlePass(Channel):
    """
    Class based system to handle the battle pass channel for the calendar service
    """

    def __init__(self) -> None:
        """
        Initialise the battle pass channel class.
        This will setup the variables for the battle pass channel
        """
        super().__init__()

    def update_events(self) -> None:
        """
        Update the events for the battle pass channel
        :return:
        """
        pass
