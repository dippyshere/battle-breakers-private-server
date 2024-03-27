"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

Handles the robots.txt file
"""
import sanic

from utils import types
from utils.sanic_gzip import Compress

compress = Compress()
robots = sanic.Blueprint("robots")


# undocumented
@robots.route("robots.txt", methods=["GET"])
@compress.compress()
async def robots_txt(request: types.BBRequest) -> sanic.response.HTTPResponse:
    """
    Get the robots.txt file

    :param request: The request object
    :return: The response object
    """
    return sanic.response.text("User-agent: *\nDisallow: \nSitemap: /sitemap.xml\n", content_type="text/plain")


@robots.route("sitemap.xml", methods=["GET"])
@compress.compress()
async def sitemap_xml(request: types.BBRequest) -> sanic.response.HTTPResponse:
    """
    Get the sitemap.xml file

    :param request: The request object
    :return: The response object
    """
    return sanic.response.text("<?xml version='1.0' encoding='UTF-8'?>\n"
                               "<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n"
                               "  <url>\n"
                               "    <loc>http://111.220.198.218/id/login</loc>\n"
                               "    <lastmod>2024-03-27</lastmod>\n"
                               "  </url>\n"
                               "</urlset>", content_type="application/xml")
