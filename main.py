"""
A Battle Breakers Private server written in Python by Dippyshere
https://github.com/Dippyshere/Battle-Breakers-Private-Server
"""

from api import api

import orjson
import sanic
import colorama

try:
    import tomllib as toml
except ModuleNotFoundError:
    import tomli as toml

colorama.init()

app = sanic.app.Sanic('dippy_breakers', dumps=orjson.dumps, loads=orjson.loads)
app.blueprint(api)

with open("config.toml", "rb") as config_file:
    config = toml.load(config_file)
    config_file.close()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8889, auto_reload=True)
