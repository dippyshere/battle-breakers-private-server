"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Class based systems for each of the storefronts in the storefront service
"""
from typing import Any, Self


class Offer:
    """
    Class based system to handle offers for a catalog entry in the storefront service
    """

    def __init__(self) -> None:
        """
        Initialise the offer class.
        This will setup the variables for the offer
        """
        self.offer_id: str = ""
        self.dev_name: str = ""
        self.offer_type: str = ""
        self.prices: list[dict[str, str | int]] = []
        self.categories: list[str] = []
        self.daily_limit: int = -1
        self.weekly_limit: int = -1
        self.monthly_limit: int = -1
        self.refundable: bool = False
        self.app_store_id: list[str] = []
        self.requirements: list[dict[str, str | int]] = []
        self.meta_info: list[dict[str, str | int]] = []
        self.catalog_group: str = ""
        self.catalog_group_priority: int = 0
        self.sort_priority: int = 0
        self.title: str = ""
        self.short_description: str = ""
        self.description: str = ""
        self.display_asset_path: str = ""
        self.item_grants: list[dict[str, str | int]] = []

    def __repr__(self) -> str:
        """
        Get the representation of the offer class
        :return: The representation of the offer class
        """
        return f"<Offer>"

    def __str__(self) -> str:
        """
        Get the string of the offer class
        :return: The string of the offer class
        """
        return self.__repr__()

    def __dict__(self) -> dict[str, Any]:
        """
        Get the dictionary of the offer class
        :return: The dictionary of the offer class
        """
        return {
            "offerId": self.offer_id,
            "devName": self.dev_name,
            "offerType": self.offer_type,
            "prices": self.prices,
            "categories": self.categories,
            "dailyLimit": self.daily_limit,
            "weeklyLimit": self.weekly_limit,
            "monthlyLimit": self.monthly_limit,
            "refundable": self.refundable,
            "appStoreId": self.app_store_id,
            "requirements": self.requirements,
            "metaInfo": self.meta_info,
            "catalogGroup": self.catalog_group,
            "catalogGroupPriority": self.catalog_group_priority,
            "sortPriority": self.sort_priority,
            "title": self.title,
            "shortDescription": self.short_description,
            "description": self.description,
            "displayAssetPath": self.display_asset_path,
            "itemGrants": self.item_grants
        }

    def __getitem__(self, key: str) -> Any:
        """
        Get the value of the key in the offer class
        :param key: The key to get the value of
        :return: The value of the key in the offer class
        """
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value of the key in the offer class
        :param key: The key to set the value of
        :param value: The value to set the key to
        :return: The value of the key in the offer class
        """
        setattr(self, key, value)

    def __delitem__(self, key: str) -> None:
        """
        Delete the key in the offer class
        :param key: The key to delete
        :return: The value of the key in the offer class
        """
        delattr(self, key)

    def __len__(self) -> int:
        """
        Get the length of the offer
        :return: The length of the offer
        """
        return len(self.__dict__())


class Storefront:
    """
    Class based system to handle a storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the storefront class.
        This will setup the variables for the storefront
        """
        self.name: str = ""
        self.catalog_entries: list[Offer] = []

    def __repr__(self) -> str:
        """
        Get the representation of the storefront class
        :return: The representation of the storefront class
        """
        return f"<Storefront>"

    def __str__(self) -> str:
        """
        Get the string of the storefront class
        :return: The string of the storefront class
        """
        return self.__repr__()

    def __dict__(self) -> dict[str, Any]:
        """
        Get the dictionary of the storefront class
        :return: The dictionary of the storefront class
        """
        catalog_entries = []
        for catalog_entry in self.catalog_entries:
            catalog_entries.append(catalog_entry.__dict__())
        return {
            "name": self.name,
            "catalogEntries": catalog_entries
        }

    def __getitem__(self, key: str) -> Any:
        """
        Get the value of the key in the storefront class
        :param key: The key to get the value of
        :return: The value of the key in the storefront class
        """
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set the value of the key in the storefront class
        :param key: The key to set the value of
        :param value: The value to set the key to
        :return: The value of the key in the storefront class
        """
        setattr(self, key, value)

    def __delitem__(self, key: str) -> None:
        """
        Delete the key in the storefront class
        :param key: The key to delete
        :return: The value of the key in the storefront class
        """
        delattr(self, key)

    def __len__(self) -> int:
        """
        Get the length of the storefront
        :return: The length of the storefront
        """
        return len(self.__dict__())


class SecretShopPage3(Storefront):
    """
    Class based system to handle the SecretShopPage3 storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the SecretShopPage3 storefront class.
        This will setup the variables for the SecretShopPage3 storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the SecretShopPage3 storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the SecretShopPage3 storefront
        :return: The initialised SecretShopPage3 storefront class
        """
        self: SecretShopPage3 = cls()
        self.name = "SecretShopPage3"
        self.catalog_entries = []
        return self


class SecretShopPage4(Storefront):
    """
    Class based system to handle the SecretShopPage4 storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the SecretShopPage4 storefront class.
        This will setup the variables for the SecretShopPage4 storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the SecretShopPage4 storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the SecretShopPage4 storefront
        :return: The initialised SecretShopPage4 storefront class
        """
        self: SecretShopPage4 = cls()
        self.name = "SecretShopPage4"
        self.catalog_entries = []
        return self


class GemStore(Storefront):
    """
    Class based system to handle the GemStore storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the GemStore storefront class.
        This will setup the variables for the GemStore storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the GemStore storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the GemStore storefront
        :return: The initialised GemStore storefront class
        """
        self: GemStore = cls()
        self.name = "GemStore"
        self.catalog_entries = []
        return self


class SecretShopPage2(Storefront):
    """
    Class based system to handle the SecretShopPage2 storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the SecretShopPage2 storefront class.
        This will setup the variables for the SecretShopPage2 storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the SecretShopPage2 storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the SecretShopPage2 storefront
        :return: The initialised SecretShopPage2 storefront class
        """
        self: SecretShopPage2 = cls()
        self.name = "SecretShopPage2"
        self.catalog_entries = []
        return self


class WeeklyChallenge(Storefront):
    """
    Class based system to handle the WeeklyChallenge storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the WeeklyChallenge storefront class.
        This will setup the variables for the WeeklyChallenge storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the WeeklyChallenge storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the WeeklyChallenge storefront
        :return: The initialised WeeklyChallenge storefront class
        """
        self: WeeklyChallenge = cls()
        self.name = "WeeklyChalllenge"
        self.catalog_entries = []
        return self


class HeroStore(Storefront):
    """
    Class based system to handle the HeroStore storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the HeroStore storefront class.
        This will setup the variables for the HeroStore storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the HeroStore storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the HeroStore storefront
        :return: The initialised HeroStore storefront class
        """
        self: HeroStore = cls()
        self.name = "HeroStore"
        self.catalog_entries = []
        return self


class Featured(Storefront):
    """
    Class based system to handle the Featured storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the Featured storefront class.
        This will setup the variables for the Featured storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the Featured storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the Featured storefront
        :return: The initialised Featured storefront class
        """
        self: Featured = cls()
        self.name = "Featured"
        self.catalog_entries = []
        return self


class SecretShop(Storefront):
    """
    Class based system to handle the SecretShop storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the SecretShop storefront class.
        This will setup the variables for the SecretShop storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the SecretShop storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the SecretShop storefront
        :return: The initialised SecretShop storefront class
        """
        self: SecretShop = cls()
        self.name = "SecretShop"
        self.catalog_entries = []
        return self


class MagicTicket(Storefront):
    """
    Class based system to handle the MagicTicket storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the MagicTicket storefront class.
        This will setup the variables for the MagicTicket storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the MagicTicket storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the MagicTicket storefront
        :return: The initialised MagicTicket storefront class
        """
        self: MagicTicket = cls()
        self.name = "MagicTicket"
        self.catalog_entries = []
        return self


class Services(Storefront):
    """
    Class based system to handle the Services storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the Services storefront class.
        This will setup the variables for the Services storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the Services storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the Services storefront
        :return: The initialised Services storefront class
        """
        self: Services = cls()
        self.name = "Services"
        self.catalog_entries = []
        return self


class Marketplace(Storefront):
    """
    Class based system to handle the Marketplace storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the Marketplace storefront class.
        This will setup the variables for the Marketplace storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the Marketplace storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the Marketplace storefront
        :return: The initialised Marketplace storefront class
        """
        self: Marketplace = cls()
        self.name = "Marketplace"
        self.catalog_entries = []
        return self


class MarketplacePage3(Storefront):
    """
    Class based system to handle the MarketplacePage3 storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the MarketplacePage3 storefront class.
        This will setup the variables for the MarketplacePage3 storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the MarketplacePage3 storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the MarketplacePage3 storefront
        :return: The initialised MarketplacePage3 storefront class
        """
        self: MarketplacePage3 = cls()
        self.name = "MarketplacePage3"
        self.catalog_entries = []
        return self


class MarketplacePage2(Storefront):
    """
    Class based system to handle the MarketplacePage2 storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the MarketplacePage2 storefront class.
        This will setup the variables for the MarketplacePage2 storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the MarketplacePage2 storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the MarketplacePage2 storefront
        :return: The initialised MarketplacePage2 storefront class
        """
        self: MarketplacePage2 = cls()
        self.name = "MarketplacePage2"
        self.catalog_entries = []
        return self


class Events(Storefront):
    """
    Class based system to handle the Events storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the Events storefront class.
        This will setup the variables for the Events storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the Events storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the Events storefront
        :return: The initialised Events storefront class
        """
        self: Events = cls()
        self.name = "Events"
        self.catalog_entries = []
        return self


class Workshop(Storefront):
    """
    Class based system to handle the Workshop storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the Workshop storefront class.
        This will setup the variables for the Workshop storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the Workshop storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the Workshop storefront
        :return: The initialised Workshop storefront class
        """
        self: Workshop = cls()
        self.name = "Workshop"
        self.catalog_entries = []
        return self


class Loyalty(Storefront):
    """
    Class based system to handle the Loyalty storefront for the storefront catalog service
    """

    def __init__(self) -> None:
        """
        Initialise the Loyalty storefront class.
        This will setup the variables for the Loyalty storefront
        """
        super().__init__()

    async def update_storefront(self) -> None:
        """
        Update the storefront for the Loyalty storefront class with the latest data
        :return: None
        """

    @classmethod
    async def init_storefront(cls) -> Self:
        """
        Initialise the Loyalty storefront
        :return: The initialised Loyalty storefront class
        """
        self: Loyalty = cls()
        self.name = "Loyalty"
        self.catalog_entries = []
        return self
