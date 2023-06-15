"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Error handler module for the server
"""
from typing import Optional

from .error_details import error_details

import uuid
import sanic
from sanic.handlers import ErrorHandler


class EpicError:
    """
    Epic error class
    """

    def __init__(self, error_code: Optional[str] = None, error_message: Optional[str] = None,
                 numeric_error_code: Optional[int] = None) -> None:
        """
        Initialises the EpicError class
        :param error_code: The error code
        :param error_message: The error message
        :param numeric_error_code: The numeric error code
        """
        self.error_code = error_code
        self.error_message = error_message
        self.numeric_error_code = numeric_error_code


class CustomErrorHandler(ErrorHandler):
    """
    Custom error handler to handle all exceptions
    """

    def default(self, request: sanic.request.Request,
                exception: sanic.exceptions.SanicException | Exception) -> sanic.response.JSONResponse:
        """
        Handles all exceptions
        :param request: The request object
        :param exception: The exception object
        :return: The response
        """
        ErrorHandler.log(request, exception)
        status_code = getattr(exception, "status_code", 500)
        message_vars = []
        for var in getattr(exception, "args", []):
            message_vars.append(var)
        error = error_details.get(status_code, {
            "error_code": "errors.com.epicgames.unknown_error.v2",
            "error_message": "An unknown error has occurred, please report to admin. 🗿",
            "numeric_error_code": 0
        })
        error_code = error["error_code"]
        error_message = error["error_message"]
        numeric_error_code = error["numeric_error_code"]
        if getattr(exception, "context", None) is not None:
            error_code = exception.context.get("errorCode", error_code)
            error_message = exception.context.get("errorMessage", error_message)
            numeric_error_code = exception.context.get("numericErrorCode", numeric_error_code)
        if True:  # request.app.debug
            if status_code == 500:
                error_message = ""
                for message in message_vars:
                    error_message += f"{message}"
            error_message += f" ({exception.__class__.__name__})"
        headers = {
            "X-Epic-Error-Code": numeric_error_code,
            "X-Epic-Error-Name": error_code,
        }
        return sanic.response.json({
            "errorCode": error_code,
            "errorMessage": error_message,
            "messageVars": message_vars,
            "numericErrorCode": numeric_error_code,
            "originatingService": "WEX",
            "intent": "prod",
            "trackingId": uuid.uuid4().__str__(),
            "errorDescription": error_message,
            "errorName": error_code.split(".")[-1],
        }, status_code, headers)
