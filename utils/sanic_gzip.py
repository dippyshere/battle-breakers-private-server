"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the MIT License.

Full credit to https://github.com/koug44/sanic-gzip/blob/master/sanic_gzip/__init__.py
Modified to work with Battle Breakers Private Server, and to add brotli support.
"""
import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps
import gzip
import zlib

import brotli
from sanic.request import Request
from sanic.response import ResponseStream

DEFAULT_MIME_TYPES = frozenset(
    [
        "text/html",
        "text/css",
        "text/xml",
        "text/plain",
        "text/text",
        "text/javascript",
        "application/json",
        "application/javascript",
        "application/manifest+json",
        "application/xml",
        "application/xhtml+xml",
        "application/rss+xml",
        "application/atom+xml",
        "font/eot",
        "font/otf",
        "font/ttf",
        "image/svg+xml"
    ]
)


class Compress(object):
    """
    Compresses response data with gzip or deflate encoding.
    """

    def __init__(
            self,
            compress_mimetypes=DEFAULT_MIME_TYPES,
            compress_level=4,
            compress_min_size=512,
            max_threads=None,
    ):

        self.executors = ThreadPoolExecutor(max_threads)
        self.config = {
            "CNT_COMPRESS_THREADS": max_threads,
            "COMPRESS_MIMETYPES": compress_mimetypes,
            "COMPRESS_LEVEL": compress_level,
            "COMPRESS_MIN_SIZE": compress_min_size,
        }

        self.gzip_func = partial(gzip.compress, compresslevel=self.config["COMPRESS_LEVEL"])
        self.zlib_func = partial(zlib.compress, level=self.config["COMPRESS_LEVEL"])
        self.br_func = partial(brotli.compress, quality=self.config["COMPRESS_LEVEL"])

    async def _gzip_compress(self, response):
        response.body = await asyncio.get_event_loop().run_in_executor(
            self.executors, self.gzip_func, response.body
        )
        response.headers["Content-Encoding"] = "gzip"
        response.headers["Content-Length"] = len(response.body)
        return response

    async def _zlib_compress(self, response):
        response.body = await asyncio.get_event_loop().run_in_executor(
            self.executors, self.zlib_func, response.body
        )
        response.headers["Content-Encoding"] = "deflate"
        response.headers["Content-Length"] = len(response.body)
        return response

    async def _br_compress(self, response):
        response.body = await asyncio.get_event_loop().run_in_executor(
            self.executors, brotli.compress, response.body
        )
        response.headers["Content-Encoding"] = "br"
        response.headers["Content-Length"] = len(response.body)
        return response

    def compress(self, f=None):
        """
        Compresses response data with brotli, gzip or deflate encoding.
        :param f: The function to decorate.
        :return: The decorated function.
        """

        def decorator(f):
            """
            Decorator for compressing response data with brotli, gzip or deflate encoding.
            :param f: The function to decorate.
            :return: The decorated function.
            """

            @wraps(f)
            async def _compress_response(*args, **kwargs):
                if isinstance(args[0], Request):
                    # Function-based endpoint
                    request = args[0]
                else:
                    # View-based endpoint with "self" as first arg
                    request = args[1]

                accept_encoding = request.headers.get("Accept-Encoding", "").lower()

                if not accept_encoding or (
                        "gzip" not in accept_encoding and "deflate" not in accept_encoding and "br" not in accept_encoding
                ):
                    return await f(*args, **kwargs)

                response = await f(*args, **kwargs)

                if type(response) is ResponseStream or not 200 <= response.status < 300:
                    return response

                content_length = len(response.body)
                content_type = response.content_type

                if content_type and ";" in content_type:
                    content_type = content_type.split(";")[0]

                if (
                        content_type not in self.config["COMPRESS_MIMETYPES"]
                        or content_length < self.config["COMPRESS_MIN_SIZE"]
                ):
                    return response

                if "br" in accept_encoding:
                    return await self._br_compress(response)

                if "gzip" in accept_encoding:
                    return await self._gzip_compress(response)

                if "deflate" in accept_encoding:
                    return await self._zlib_compress(response)

                return response

            return _compress_response

        return decorator
