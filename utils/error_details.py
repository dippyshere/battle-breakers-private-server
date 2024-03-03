"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2024 by Alexander Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the Breakers Revived License (BRL).

This file contains generic error details for the server categorised by HTTP status code.
"""

error_details = {
    400: {
        "error_code": "errors.com.epicgames.common.bad_request",
        "error_message": "Sorry the request you made was invalid",
        "numeric_error_code": 1006
    },
    401: {
        "error_code": "errors.com.epicgames.common.authentication.authentication_failed",
        "error_message": "Sorry you are not authenticated to access this resource",
        "numeric_error_code": 1032
    },
    402: {
        "error_code": "errors.com.epicgames.common.payment_required",
        "error_message": "Sorry you need to pay to access this resource",
        "numeric_error_code": 1022
    },
    403: {
        "error_code": "errors.com.epicgames.common.forbidden",
        "error_message": "Sorry you are not allowed to access this resource",
        "numeric_error_code": 1023
    },
    404: {
        "error_code": "errors.com.epicgames.common.not_found",
        "error_message": "Sorry the resource you were trying to find could not be found",
        "numeric_error_code": 1004
    },
    405: {
        "error_code": "errors.com.epicgames.common.method_not_allowed",
        "error_message": "Sorry the resource you were trying to access cannot be accessed with the HTTP method you used.",
        "numeric_error_code": 1009
    },
    406: {
        "error_code": "errors.com.epicgames.common.none_acceptable",
        "error_message": "Proxy authentication required",
        "numeric_error_code": 1010
    },
    407: {
        "error_code": "errors.com.epicgames.common.proxy_authentication_required",
        "error_message": "The server timed out waiting for the request",
        "numeric_error_code": 1011
    },
    408: {
        "error_code": "errors.com.epicgames.common.request_timeout",
        "error_message": "The server timed out waiting for the request",
        "numeric_error_code": 1012
    },
    409: {
        "error_code": "errors.com.epicgames.common.conflict",
        "error_message": "Sorry there was a conflict with the current state of the resource",
        "numeric_error_code": 1013
    },
    410: {
        "error_code": "errors.com.epicgames.common.gone",
        "error_message": "Sorry the resource you were trying to find is no longer available",
        "numeric_error_code": 1014
    },
    411: {
        "error_code": "errors.com.epicgames.common.length_required",
        "error_message": "Sorry the server requires a content length header",
        "numeric_error_code": 1015
    },
    412: {
        "error_code": "errors.com.epicgames.common.precondition_failed",
        "error_message": "Sorry the precondition given in the request evaluated to false by the server",
        "numeric_error_code": 1016
    },
    413: {
        "error_code": "errors.com.epicgames.common.request_entity_too_large",
        "error_message": "Sorry the server will not accept the request because the request entity is too large",
        "numeric_error_code": 1017
    },
    414: {
        "error_code": "errors.com.epicgames.common.request_uri_too_long",
        "error_message": "Sorry the server will not accept the request because the URL is too long",
        "numeric_error_code": 1018
    },
    415: {
        "error_code": "errors.com.epicgames.common.unsupported_media_type",
        "error_message": "Sorry your request could not be processed as you are supplying a media type we do not support",
        "numeric_error_code": 1006
    },
    416: {
        "error_code": "errors.com.epicgames.common.requested_range_not_satisfiable",
        "error_message": "Sorry the server cannot provide the requested range",
        "numeric_error_code": 1020
    },
    417: {
        "error_code": "errors.com.epicgames.common.expectation_failed",
        "error_message": "Sorry the server cannot meet the requirements of the Expect request-header field",
        "numeric_error_code": 1021
    },
    418: {
        "error_code": "errors.com.epicgames.common.im_a_teapot",
        "error_message": "Sorry the server is a teapot",
        "numeric_error_code": 1022
    },
    422: {
        "error_code": "errors.com.epicgames.common.unprocessable_entity",
        "error_message": "Sorry the server understands the content type of the request entity but was unable to process the contained instructions",
        "numeric_error_code": 1024
    },
    423: {
        "error_code": "errors.com.epicgames.common.locked",
        "error_message": "Sorry the operation could not be completed because the resource is locked",
        "numeric_error_code": 1025
    },
    424: {
        "error_code": "errors.com.epicgames.common.failed_dependency",
        "error_message": "Sorry the method could not be performed because the requested action depended on another action and that action failed",
        "numeric_error_code": 1026
    },
    425: {
        "error_code": "errors.com.epicgames.common.unordered_collection",
        "error_message": "Sorry the server is unwilling to accept the request without a defined Content-Length header",
        "numeric_error_code": 1027
    },
    426: {
        "error_code": "errors.com.epicgames.common.upgrade_required",
        "error_message": "Sorry the server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol",
        "numeric_error_code": 1028
    },
    428: {
        "error_code": "errors.com.epicgames.common.precondition_required",
        "error_message": "Sorry the server requires the request to be conditional",
        "numeric_error_code": 1029
    },
    429: {
        "error_code": "errors.com.epicgames.common.throttled",
        "error_message": "Please... slow down. I'm just a simple computer and I can only do so much.",
        "numeric_error_code": 1041
    },
    431: {
        "error_code": "errors.com.epicgames.common.request_header_fields_too_large",
        "error_message": "Sorry the server is unwilling to process the request because its header fields are too large",
        "numeric_error_code": 1030
    },
    449: {
        "error_code": "errors.com.epicgames.common.retry_with",
        "error_message": "Sorry the request should be retried after doing the appropriate action",
        "numeric_error_code": 1031
    },
    451: {
        "error_code": "errors.com.epicgames.common.unavailable_for_legal_reasons",
        "error_message": "Sorry the server is unavailable for legal reasons",
        "numeric_error_code": 1032
    },
    500: {
        "error_code": "errors.com.epicgames.common.server_error",
        "error_message": "Sorry an error occurred and we were unable to resolve it",
        "numeric_error_code": 1000
    },
    501: {
        "error_code": "errors.com.epicgames.common.not_implemented",
        "error_message": "Sorry the requested method is not implemented by the server",
        "numeric_error_code": 1001
    },
    502: {
        "error_code": "errors.com.epicgames.common.bad_gateway",
        "error_message": "Sorry the server received an invalid response from an upstream server",
        "numeric_error_code": 1002
    },
    503: {
        "error_code": "errors.com.epicgames.common.service_unavailable",
        "error_message": "Sorry the server is currently unavailable",
        "numeric_error_code": 1003
    },
    504: {
        "error_code": "errors.com.epicgames.common.gateway_timeout",
        "error_message": "Sorry the server did not receive a timely response from an upstream server",
        "numeric_error_code": 1004
    },
    505: {
        "error_code": "errors.com.epicgames.common.http_version_not_supported",
        "error_message": "Sorry the server does not support the HTTP protocol version used in the request",
        "numeric_error_code": 1005
    },
    506: {
        "error_code": "errors.com.epicgames.common.variant_also_negotiates",
        "error_message": "Sorry the server has an internal configuration error:  the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process",
        "numeric_error_code": 1006
    },
    507: {
        "error_code": "errors.com.epicgames.common.insufficient_storage",
        "error_message": "Sorry the method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request",
        "numeric_error_code": 1007
    },
    508: {
        "error_code": "errors.com.epicgames.common.loop_detected",
        "error_message": "Sorry the server detected an infinite loop while processing the request",
        "numeric_error_code": 1008
    },
    509: {
        "error_code": "errors.com.epicgames.common.bandwidth_limit_exceeded",
        "error_message": "Sorry the server has exceeded the bandwidth specified by the server administrator; please try again later",
        "numeric_error_code": 1009
    },
    510: {
        "error_code": "errors.com.epicgames.common.not_extended",
        "error_message": "Sorry the server is not able to process the request because the method used is not supported by the server and it cannot be handled by the protocol",
        "numeric_error_code": 1010
    },
    511: {
        "error_code": "errors.com.epicgames.common.network_authentication_required",
        "error_message": "Sorry the client needs to authenticate to gain network access",
        "numeric_error_code": 1011
    },
    598: {
        "error_code": "errors.com.epicgames.common.network_read_timeout_error",
        "error_message": "Sorry the network read timeout error has occurred",
        "numeric_error_code": 1012
    },
    599: {
        "error_code": "errors.com.epicgames.common.network_connect_timeout_error",
        "error_message": "Sorry the network connect timeout error has occurred",
        "numeric_error_code": 1013
    }
}
