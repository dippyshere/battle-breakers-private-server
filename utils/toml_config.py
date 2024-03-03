"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles loading the toml config into the Sanic application
"""
from typing import Any

import sanic

try:
    import tomllib as toml
except ModuleNotFoundError:
    import tomli as toml


class TomlConfig(sanic.config.Config):
    def __init__(self, *args, path: str, **kwargs) -> None:
        """
        Load a TOML config file
        :param args: The args
        :param path: The path to the TOML config file
        :param kwargs: The kwargs
        """
        super().__init__(*args, **kwargs)

        with open(path, "rb") as f:
            self.apply(toml.load(f))
            f.close()

    def apply(self, config: dict[str, Any]) -> None:
        """
        Apply the TOML config to the Sanic config
        :param config: The TOML config
        """
        self.update(self._to_uppercase(config))

    def _to_uppercase(self, obj: dict[str, Any]) -> dict[str, Any]:
        retval: dict[str, Any] = {}
        for key, value in obj.items():
            upper_key = key.upper()
            if isinstance(value, list):
                retval[upper_key] = [
                    self._to_uppercase(item) for item in value
                ]
            elif isinstance(value, dict):
                retval[upper_key] = self._to_uppercase(value)
            else:
                retval[upper_key] = value
        return retval
