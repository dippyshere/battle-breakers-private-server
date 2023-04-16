"""
A Battle Breakers Private server written in Python by Dippyshere
https://github.com/Dippyshere/Battle-Breakers-Private-Server
"""

from api import api

import orjson
import sanic
import sanic_ext
import colorama

import datetime
import uuid

try:
    import tomllib as toml
except ModuleNotFoundError:
    import tomli as toml

colorama.init()

app = sanic.app.Sanic('dippy_breakers', dumps=orjson.dumps, loads=orjson.loads)
app.config.CORS_ORIGINS = "*"
app.config.CORS_ALWAYS_SEND = True
app.blueprint(api)
sanic_ext.Extend(app)

with open("config.toml", "rb") as config_file:
    config = toml.load(config_file)
    config_file.close()


@app.middleware("response")
async def add_mcp_headers(request, response):
    """
    Adds the standard MCP headers to the response

    :param request: The request object
    :param response: The response object
    :return: None
    """
    try:
        content_version = request.headers.get('X-EpicGames-WEX-BuildVersion')
    except:
        try:
            content_version = request.headers.get('User-Agent').split('build=')[1]
        except:
            content_version = "1.88.244-r17036752"
    try:
        corrid = request.headers.get('X-Epic-Correlation-ID')
    except:
        try:
            corrid = request.id
        except:
            corrid = str(uuid.uuid4())
    response.headers["Date"] = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    response.headers["X-EpicGames-McpVersion"] = "prod Release-1.88-1.88 build 107 cl 19310354"
    response.headers["X-EpicGames-ContentVersion"] = content_version
    response.headers["X-EpicGames-MinBuild"] = "-1"
    response.headers["X-Epic-Correlation-ID"] = corrid

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, auto_reload=True)
