"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Class based system to handle the calendar services
"""
import datetime
from typing import Any

import utils.services.calendar.channels as channels


class ScheduledEvents:
    """
    Class based system to handle the calendar services
    """

    def __init__(self) -> None:
        """
        Initialise the scheduled events class.
        This will setup the variables for the calendar
        """
        self.updated: datetime = datetime.datetime.utcnow()
        self.news: channels.News = channels.News()
        self.limited_time_mode: channels.LimitedTimeMode = channels.LimitedTimeMode()
        self.marketing: channels.Marketing = channels.Marketing()
        self.rotational_content: channels.RotationalContent = channels.RotationalContent()
        self.featured_stores_mcp: channels.FeaturedStoresMcp = channels.FeaturedStoresMcp()
        self.weekly_challenge: channels.WeeklyChallenge = channels.WeeklyChallenge()
        self.battlepass: channels.BattlePass = channels.BattlePass()

    def __repr__(self) -> str:
        """
        Get the representation of the ScheduledEvents class
        :return: The representation of the ScheduledEvents class
        """
        return f"<ScheduledEvents>"

    def __str__(self) -> str:
        """
        Get the string of the ScheduledEvents class
        :return: The string of the ScheduledEvents class
        """
        return self.__repr__()

    def __dict__(self) -> dict[str, Any]:
        """
        Get the dictionary of the ScheduledEvents class
        :return: The dictionary of the ScheduledEvents class
        """
        return {
            "news": self.news.__dict__(),
            "limited-time-mode": self.limited_time_mode.__dict__(),
            "marketing": self.marketing.__dict__(),
            "rotational-content": self.rotational_content.__dict__(),
            "featured-stores-mcp": self.featured_stores_mcp.__dict__(),
            "weekly-challenge": self.weekly_challenge.__dict__(),
            "battlepass": self.battlepass.__dict__()
        }

    def __getitem__(self, key: str) -> Any:
        """
        Get the value of the key in the ScheduledEvents class
        :param key: The key to get the value of
        :return: The value of the key in the ScheduledEvents class
        """
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value of the key in the ScheduledEvents class
        :param key: The key to set the value of
        :param value: The value to set the key to
        :return: The value of the key in the ScheduledEvents class
        """
        setattr(self, key, value)

    def __delitem__(self, key: str) -> None:
        """
        Delete the key in the ScheduledEvents class
        :param key: The key to delete
        :return: The value of the key in the ScheduledEvents class
        """
        delattr(self, key)

    def __len__(self) -> int:
        """
        Get the length of the ScheduledEvents
        :return: The length of the ScheduledEvents
        """
        return len(self.__dict__())

    def update_events(self) -> None:
        """
        Update the events in the ScheduledEvents class
        :return: None
        """
        self.updated = datetime.datetime.utcnow()
        self.news.update_events()
        self.limited_time_mode.update_events()
        self.marketing.update_events()
        self.rotational_content.update_events()
        self.featured_stores_mcp.update_events()
        self.weekly_challenge.update_events()
        self.battlepass.update_events()
