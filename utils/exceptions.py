"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Error exceptions class for formatting error responses
"""
from typing import Any


class EpicException(Exception):
    """
    The base exception class for all Epic exceptions
    """

    _quiet: bool = True

    errorCode: str = None
    errorMessage: str = None
    messageVars: list = []
    numericErrorCode: int = 0
    originatingService: str = None
    intent: str = "prod"
    trackingId: str = None
    statusCode: int = 400
    error_description: str = None
    error: str = None
    validationFailures: dict[str, dict[str, str | dict[str, str]]] = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if self.errorCode is None:
            self.errorCode: str = self.__class__.__qualname__
        for key, value in kwargs.items():
            setattr(self, key, value)
        if args:
            self.errorMessage: str = self.errorMessage.format(*args)
        if self.errorMessage:
            self.messageVars: list = list(args)
        if self.error is None:
            self.error: str = type(self).__name__
        self.error_description: str = self.errorMessage
        super().__init__(self.errorMessage)

    # noinspection IncorrectFormatting
    def __dict__(self) -> dict:
        error: dict = {}
        for cls in reversed(self.__class__.__mro__):
            for attr, value in cls.__dict__.items():
                if not callable(getattr(self, attr)) and getattr(self, attr, None) is not None and not attr.startswith(
                        "_") and attr not in ["args", "quiet"]:
                    error[attr]: str | int | list | dict = getattr(self, attr)
        return error

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} errorCode={self.errorCode} errorMessage={self.errorMessage} " \
               f"numericErrorCode={self.numericErrorCode}>"

    def __str__(self) -> str:
        return self.__repr__()

    def as_dict(self) -> dict:
        """
        Returns the exception as a dictionary
        """
        return self.__dict__()

    @property
    def quiet(self) -> bool:
        """
        Returns whether the exception should be quiet or not
        :return: Whether the exception should be quiet or not
        """
        return self._quiet


class errors:
    """
    Parent class for all error classes
    """

    class com:
        """
        Parent class for all error classes
        """

        class epicgames(EpicException):
            """
            Parent class for all Epic Games error classes
            """
            errorCode: str = "errors.com.epicgames."
            errorMessage: str = "There was an error"

            class account:
                """
                Parent class for all account errors
                """

                class account_age_verification_incomplete(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class account_created_but_banned(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class account_creation_disabled(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class account_locked(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class account_locked_for_update(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class account_not_active(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry the account you are using is not active."
                    numericErrorCode: int = 18006
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 401

                class account_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry, we couldn't find an account for {0}"
                    numericErrorCode: int = 18007
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 404

                class account_permission_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class account_updated_but_banned(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class address:
                    """
                    Parent class for all address errors
                    """

                    class address_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class auth_app:
                    """
                    Parent class for all authentication app errors
                    """

                    class bad_definition_format(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class internal_client_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class not_authorized_for_account(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class auth_token:
                    """
                    Parent class for all authentication token errors
                    """

                    class invalid_access_token(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_platform_token(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_refresh_token(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class not_own_session_removal(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class unknown_oauth_session(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class unknown_oauth_session_refresh(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class banned_by_whitelist_entry(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class bulk_pwd_max_items_limit(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class cannot_change_account_status(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class client:
                    """
                    Parent class for all client errors
                    """

                    class client_permission_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class client_secret_limit_exceeded(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class client_secret_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class duplicate_client(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class duplicate_client_permission(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class duplicate_client_permissions(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class unknown_client(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class client_disabled(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry the client you are using has been disabled"
                    numericErrorCode: int = 18014
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class client_locked_for_update(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class client_missing_redirect_url(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class country_unchanged(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class device_auth:
                    """
                    Parent class for all device auth errors
                    """

                    class disabled(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_device_info(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Invalid device info JSON value"
                        numericErrorCode: int = 18130
                        originatingService: str = "com.epicgames.account.public"

                class display_name_already_set(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class display_name_change_timeframe(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class display_name_was_used(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class duplicate_account_permission(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class duplicate_display_name(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "This Name is already taken."
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class duplicate_email(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class duplicate_external_auth_type(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class duplicate_username(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class email:
                    """
                    Parent class for all email errors
                    """

                    class alternate_email_limit_exceeded(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class email_already_on_account(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class email_change_timeframe(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class email_code:
                    """
                    Parent class for all email code errors
                    """

                    class code_not_for_your_account(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class code_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class code_not_valid(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class email_code_expired(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class validation_code_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class email_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class ext_auth:
                    """
                    Parent class for all external auth errors
                    """

                    class access_revoked(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_cert(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_external_auth_token(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_token(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 1014
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 403

                    class linking_restricted(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class login_not_allowed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class missing_data(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class missing_scope(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class token_expired(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class unknown_external_auth_type(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class external_auth:
                        """
                        Parent class for all external auth errors
                        """

                        class remove(EpicException):
                            """
                            Parent class for all external auth removal errors
                            """

                            class forbid(EpicException):
                                """
                                Parent class for all forbidden external auth errors
                                """

                                class last_trusted_ext_auth_facebook(EpicException):
                                    """
                                    docstring
                                    """
                                    errorMessage: str = "message"
                                    numericErrorCode: int = 0
                                    originatingService: str = "com.epicgames.account.public"
                                    statusCode: int = 400

                                class last_trusted_ext_auth_google(EpicException):
                                    """
                                    docstring
                                    """
                                    errorMessage: str = "message"
                                    numericErrorCode: int = 0
                                    originatingService: str = "com.epicgames.account.public"
                                    statusCode: int = 400

                                class last_trusted_ext_auth_vk(EpicException):
                                    """
                                    docstring
                                    """
                                    errorMessage: str = "message"
                                    numericErrorCode: int = 0
                                    originatingService: str = "com.epicgames.account.public"
                                    statusCode: int = 400

                class external_auth_account_id_mismatch(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class external_auth_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class external_auth_restriction_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class external_auth_validate_failed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class full_account_auth_data_required(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class invalid_account_credentials(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry the account credentials you are using are invalid"
                    numericErrorCode: int = 18031
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class invalid_account_id_count(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry, the number of account id should be at least one and not more than {0}."
                    numericErrorCode: int = 18066
                    originatingService: str = "com.epicgames.account.public"

                class invalid_client_credentials(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry the client credentials you are using are invalid"
                    numericErrorCode: int = 18033
                    originatingService: str = "com.epicgames.account.public"

                class invalid_count(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class invalid_start(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class keyring(EpicException):
                    """
                    Parent class for all keyring errors
                    """

                    class unknown_keyring(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class key:
                    """
                    Parent class for all keu errors
                    """

                    class key_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class merge:
                    """
                    Parent class for all account merging errors
                    """

                    class destination_account_not_full(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class external_auth_conflict(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_account_status(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_apps(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class not_internal_client(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class source_account_not_headless(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class metadata:
                    """
                    Parent class for all account metadata errors
                    """

                    class too_many_keys(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class metadata_key_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class no_account_found_for_external_auth(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class oauth:
                    """
                    Parent class for all oauth auth errors
                    """

                    class authorization_code_not_for_your_client(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class authorization_code_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry the authorization code you supplied was not found. It is possible " \
                                            "that it was no longer valid"
                        numericErrorCode: int = 18059
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class authorization_pending(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "The authorization server request is still pending as the end user has " \
                                            "yet to visit and enter the verification code."
                        numericErrorCode: int = 1012
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class code_not_valid_for_login_type(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class exchange_code_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry the exchange code you supplied was not found. It is possible that" \
                                            " it was no longer valid"
                        numericErrorCode: int = 18057
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class expired_authorization_code(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class expired_exchange_code(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry the exchange_code has expired."
                        numericErrorCode: int = 18128
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 401

                    class expired_exchange_code_session(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry the originating session for the exchange_code has expired."
                        numericErrorCode: int = 18128
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 401

                    class missing_real_id_association(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Real ID association is required to proceed"
                        numericErrorCode: int = 18109
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 403

                    class parental_control(EpicException):
                        """
                        Parent class for all parental control errors
                        """

                        class playing_forbidden(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "com.epicgames.account.public"
                            statusCode: int = 400

                    class password_reset_required(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class single_use_code_expired(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class single_use_code_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class token_exchange_not_allowed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class too_many_sessions(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry too many sessions have been issued for your account. Please try " \
                                            "again later"
                        numericErrorCode: int = 18048
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 403

                class old_password_reuse(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class password_required(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class real_id(EpicException):
                    """
                    Parent class for all real identification errors
                    """

                    class country_change_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class remove_default_email(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class role:
                    """
                    Parent class for all account role errors
                    """

                    class duplicate_role_creation(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class duplicate_role_mapping(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_role_assignment(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class role_in_use_cannot_be_deleted(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class role_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class role_permission_not_deleted_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class role_locked_for_delete(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class role_locked_for_update(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class sdn:
                    """
                    Parent class for all sdn errors
                    """

                    class challenge_not_allowed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class disabled(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class link_github_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class sync_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class update_failed_due_to_sdn(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class update_not_allowed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class single_use_password:
                    """
                    Parent class for all single use password errors
                    """

                    class conflict(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class throttled(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Operation access is limited by throttling policy, please try again in {0} " \
                                        "second(s)."
                    numericErrorCode: int = 1041
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 429

                class token_account_id_does_not_match_url_accountId(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "The accountId supplied in the url does not match the accountId for the " \
                                        "OAuth token."
                    numericErrorCode: int = 18055
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class white_list:
                    """
                    Parent class for all account white list errors
                    """

                    class duplicate_white_list_entry(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class white_list_entry_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class xbl:
                    """
                    Parent class for all xbox live account errors
                    """

                    class invalid_token(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class invalid_token_date(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

            class bad_request(EpicException):
                """
                docstring
                """
                errorMessage: str = "Sorry the request you made was invalid"
                numericErrorCode: int = 1006
                originatingService: str = "WEX"
                statusCode: int = 400

            class catalog_helper:
                """
                docstring
                """

                class unable_to_parse_receipts(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class chat:
                """
                docstring
                """

                class forbidden_chat_operation(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_room_settings(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class room_creation_conflict(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class room_creation_failed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class room_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class xmpp_connection_error(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class cloudstorage:
                """
                docstring
                """

                class connection_close_failed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class data_read(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class duplicate_system_file(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class file_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_storage_size(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_user_storage_data(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_window_dates(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class new_quota_below_current_usage(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class user_storage_data_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class window_dates_required(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class coderedemption:
                """
                docstring
                """

                class code_used(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Code used; code:{0}"
                    numericErrorCode: int = 19010
                    originatingService: str = "com.epicgames.coderedemption.public"
                    statusCode: int = 400

            class common:
                """
                docstring
                """

                class argus:
                    """
                    docstring
                    """

                    class vulnerable_credentials(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                class authentication:
                    """
                    docstring
                    """

                    class authentication_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Authentication failed for {0}"
                        numericErrorCode: int = 1032
                        statusCode: int = 401

                    class invalid_client_service(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class token_verification_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry we couldn't validate your token {0}. Please try with a new token."
                        numericErrorCode: int = 1031
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class unable_to_retrieve_perms(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                class bad_gateway(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class concurrent_modification_error(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class duplicate_entry(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class early_eof(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class http_request_timeout(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class json_mapping_error(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Json mapping failed."
                    numericErrorCode: int = 1019

                class json_parse_error(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Json parse failed."
                    numericErrorCode: int = 1019

                class json_payload_required(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Json payload is required."
                    numericErrorCode: int = 1020

                class method_not_allowed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry the resource you were trying to access cannot be accessed with the " \
                                        "HTTP method you used."
                    numericErrorCode: int = 1009
                    originatingService: str = "WEX"
                    statusCode: int = 405

                class missing_permission(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry your login does not posses the permissions '{0} {1}' needed to " \
                                        "perform the requested operation"
                    numericErrorCode: int = 1023
                    statusCode: int = 403

                class missing_action(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Login is banned or does not posses the action '{0}' needed to perform the " \
                                        "requested operation for platform '{1}'"
                    numericErrorCode: int = 1023
                    statusCode: int = 403

                class mongo_execution_timeout_error(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry, there was a timeout utilizing the database."
                    numericErrorCode: int = 1045

                class not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Sorry the resource you were trying to find could not be found"
                    numericErrorCode: int = 1004
                    statusCode: int = 404

                class oauth:
                    """
                    docstring
                    """

                    class invalid_client(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry the client credentials you are using are invalid"
                        numericErrorCode: int = 18033
                        originatingService: str = "com.epicgames.account.public"

                    class invalid_grant(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class invalid_request(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class invalid_token(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class oauth_error(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class unauthorized_client(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry your client is not allowed to use the grant type token_to_token"
                        numericErrorCode: int = 1015
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                    class unsupported_grant_type(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Sorry, your client does not have the proper grant_type for access."
                        numericErrorCode: int = 1016
                        originatingService: str = "com.epicgames.account.public"
                        statusCode: int = 400

                class oauth_account_authentication_required(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class oauth_authentication_required(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "com.epicgames.account.public"
                    statusCode: int = 400

                class request_not_acceptable(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class throttled(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Server have no capacity to serve request for API group {0}."
                    numericErrorCode: int = 1041
                    statusCode: int = 429

                class timeout(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class two_factor_authentication(EpicException):
                    """
                    docstring
                    """

                    class required(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class verification_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

            class conflict(EpicException):
                """
                docstring
                """
                errorMessage: str = "message"
                numericErrorCode: int = 0
                originatingService: str = "WEX"
                statusCode: int = 400

            class couldstorage:
                """
                docstring
                """

                class file_move_failed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_account_id(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_user_file(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class out_of_user_space(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class user_file_post_move_delete_failed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class datarouter:
                """
                docstring
                """

                class request_limit_reached(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class ecommerce:
                """
                docstring
                """

                class affiliate:
                    """
                    docstring
                    """

                    class not_whitelisted(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                class fulfillment:
                    """
                    docstring
                    """

                    class code:
                        """
                        docstring
                        """

                        class criteria:
                            """
                            docstring
                            """

                            class reject(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                    class integration:
                        """
                        docstring
                        """

                        class entitlement:
                            """
                            docstring
                            """

                            class jwt:
                                """
                                docstring
                                """

                                class entitlement_not_found(EpicException):
                                    """
                                    docstring
                                    """
                                    errorMessage: str = "message"
                                    numericErrorCode: int = 0
                                    originatingService: str = "WEX"
                                    statusCode: int = 400

                        class invalid_parameter(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

            class forbidden(EpicException):
                """
                docstring
                """
                errorMessage: str = "Sorry your login does not posses the permissions '{0} {1}' needed to " \
                                    "perform the requested operation"
                numericErrorCode: int = 1023
                statusCode: int = 403

            class friends:
                """
                docstring
                """

                class cannot_friend_due_to_target_settings(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class duplicate_friendship(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class execution_failed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class friend_request_already_sent(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class friendship_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_connection_source_name(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_friendship(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class no_external_auth_profile_id(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class recent_players_events_disabled(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class user_list_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class user_list_not_supported(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class user_not_found_in_list(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class identity:
                """
                docstring
                """

                class realid:
                    """
                    docstring
                    """

                    class account_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                        class auth:
                            """
                            docstring
                            """

                            class failed(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                        class link_epic_account:
                            """
                            docstring
                            """

                            class already_linked(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class max_linked_accounts_restriction(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class not_linked(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class operation_conflict(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class token_account_mismatch(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                        class link_minor:
                            """
                            docstring
                            """

                            class adult_age_group(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class birthday_mismatch(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class guardian_age(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class guardian_exists(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class guardian_not_linked(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class link_foreignor_forbidden(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class max_linked_minors_restriction(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class operation_conflict(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                            class realname_mismatch(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                    class minor_not_linked(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class no_guardian(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class result_verification:
                        """
                        docstring
                        """

                        class client_error:
                            """
                            docstring
                            """

                            class authentication_attempts_exceeded(EpicException):
                                """
                                docstring
                                """
                                errorMessage: str = "message"
                                numericErrorCode: int = 0
                                originatingService: str = "WEX"
                                statusCode: int = 400

                        class decrypt_error(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "Unable to decrypt verification result: [{0}] by reason of : [{1}]"
                            numericErrorCode: int = 43001

                        class invalid_birthday(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                        class invalid_format(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                        class invalid_nationality(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                        class invalid_response(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                        class missing_required_data(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                        class server_error(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "Sorry an error occurred and we were unable to resolve it (tracking " \
                                                "id: [{0}])"
                            numericErrorCode: int = 1000
                            statusCode: int = 500

                    class timetable:
                        """
                        docstring
                        """

                        class compulsory_shutdown_time_override(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                        class no_timetable_for_adult(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                        class wrong_format(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                    class token_verify_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class under_12(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class update:
                        """
                        docstring
                        """

                        class email_is_used(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

                        class email_not_allowed_for_minors(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "WEX"
                            statusCode: int = 400

            class launcher:
                """
                docstring
                """

                class not_entitled(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "missing entitlement."
                    numericErrorCode: int = 30000
                    originatingService: str = "launcher-service"

            class links:
                """
                docstring
                """

                class creator_name_required(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class mcpcataloghelper(EpicException):
                """
                docstring
                """
                errorMessage: str = "message"
                numericErrorCode: int = 0
                originatingService: str = "WEX"
                statusCode: int = 400

            class mcpprofilegroup(EpicException):
                """
                docstring
                """
                errorMessage: str = "message"
                numericErrorCode: int = 0
                originatingService: str = "WEX"
                statusCode: int = 400

                class no_service_permissions(EpicException):
                    """
                    dosctring
                    """
                    errorMessage: str = "Unable to find service permissions for server."
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class modules:
                """
                docstring
                """

                class gameplayutils:
                    """
                    docstring
                    """

                    class recipe_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Insufficient materials to foil this character."
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                class gamesubcatalog:
                    """
                    docstring
                    """

                    class gift_recipient_not_eligible(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class purchase_not_allowed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Could not purchase catalog offer {0}, item {1} x {2} (exceeding the " \
                                            "limit of {3})"
                        numericErrorCode: int = 28004
                        originatingService: str = "WEX"

                    class validation_info_expired(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                class matchmaking:
                    """
                    docstring
                    """

                    class too_few_players(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                class messaging:
                    """
                    docstring
                    """

                    class cannot_send_to_yourself(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class message_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                class profile:
                    """
                    docstring
                    """

                    class account_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class data_delete_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class data_move_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class invalid_account_id_param(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class invalid_payload(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Unable to parse command {0}. {1}"
                        numericErrorCode: int = 12806
                        originatingService: str = "WEX"

                    class invalid_profile_command(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "{0} is not valid on {1} profiles ({2})"
                        numericErrorCode: int = 12801
                        originatingService: str = "WEX"

                    class invalid_profile_id_param(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class operation_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "Operation {0} not found"
                        numericErrorCode: int = 12813
                        originatingService: str = "WEX"

                    class profile_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class template_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

            class not_found(EpicException):
                """
                docstring
                """
                errorMessage: str = "Sorry the resource you were trying to find could not be found"
                numericErrorCode: int = 1004
                statusCode: int = 404

            class ogf:
                """
                docstring
                """

                class sidecar:
                    """
                    docstring
                    """

                    class dss(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class inventory(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

            class online:
                """
                docstring
                """

                class generic(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class oss:
                """
                docstring
                """

                class accountmapping(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class availability(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class catalog(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class chat(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class entitlements(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class eula(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class externalui(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class friend(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class gameaccess(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class gameservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class groups(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class identity(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class images(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class links(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class messages(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlineaccessmcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlineaffiliatemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinebuildinfoservicemcpv2(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinechannelsservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinecoderedemptionservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlineconnectionstatusmcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinecontentcontrolsservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinedatastorageservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinedevicenotificationservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinediscovery(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlineeventsservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinefulfillmentservice(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinegiftservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinehandoverservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinemeshemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinemessagestorageservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinesidecarmcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinesocialbanservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinestats(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                    class disabled(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class invalid_leaderboard_specified(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class invalid_user_specified(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class no_stats_specified(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class no_users_specified(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class payload_empty(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                    class request_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "WEX"
                        statusCode: int = 400

                class onlinestatsingestionservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinestompconnectionmanagermcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinetime(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class onlinetssproxyservicemcp(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class orders(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class party(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class payment(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class presence(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class priceengine(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class purchase(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class session(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class store(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class titlefile(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class turnauth(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class usercloud(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class users(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class waitingroom(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class purchase:
                """
                docstring
                """

                class no_new_entitlements_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class redemption_failed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

            class server_error(EpicException):
                """
                docstring
                """
                errorMessage: str = "message"
                numericErrorCode: int = 0
                originatingService: str = "WEX"
                statusCode: int = 400

            class service_unavailable(EpicException):
                """
                docstring
                """
                errorMessage: str = "message"
                numericErrorCode: int = 0
                originatingService: str = "WEX"
                statusCode: int = 400

            class social:
                """
                docstring
                """

                class activity:
                    """
                    docstring
                    """

                    class account_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class bad_request:
                        """
                        docstring
                        """

                        class likes_feed_not_supported(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                    class conflict:
                        """
                        docstring
                        """

                        class concurrent_post_modification(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class subscriptions_limit_reached(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                    class execution_failed(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class forbidden:
                        """
                        docstring
                        """

                        class account_token_request_only(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class activity_access_forbidden(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class channel_post_forbidden(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class delete_non_post_activity_forbidden(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class delete_post_forbidden(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class own_channel_unsubscription_forbidden(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                    class friend_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class friendship_exist(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class invalid_arguments(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class invalid_credential(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                        class activity_not_found(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class subscription_not_found(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class unknown_channel(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                class group:
                    """
                    docstring
                    """

                    class not_found:
                        """
                        docstring
                        """

                        class tag(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                class groups:
                    """
                    docstring
                    """

                    class bad_request:
                        """
                        docstring
                        """

                        class invalid_metadata_key(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class user_not_identified(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                    class conflict:
                        """
                        docstring
                        """

                        class blocked_user(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class concurrent_group_details_modification(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class concurrent_job_modification(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class concurrent_member_info_modification(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class concurrent_metadata_modification(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class concurrent_profile_modification(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class duplicate_name(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class existing_member(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class headcount_limit_exceeded(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class invite_only_group(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class membership_limit_exceeded(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class pending_application(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class pending_invitation(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                    class forbidden:
                        """
                        docstring
                        """

                        class group_authorize(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class job_state(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class private_group(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                    class not_found:
                        """
                        docstring
                        """

                        class admin(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class application(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class block(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class group(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class invitation(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class member(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                        class metadata(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                class party(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "party"
                    statusCode: int = 400

                    class account_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class appid_does_not_match(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class applicant_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class connection_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class invalid_connection_offline_ttl(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class invite_already_exists(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class invite_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class invite_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class invite_status_change_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class member_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class member_state_change_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class party_change_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class party_is_full(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class party_join_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "The user {0} has no right to join party {1}."
                        numericErrorCode: int = 51006
                        originatingService: str = "party"
                        statusCode: int = 400

                    class party_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class party_query_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class ping_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class ping_not_found(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class response:
                        """
                        docstring
                        """

                        class missing_required_fields(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

                    class self_ping(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class stale_revision(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class too_many_connections(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class user_already_in_party(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class user_has_no_party(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "User [{0}] is already in a party with deployment id [{1}]."
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class user_has_party(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                    class user_is_offline(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "User [{0}] is offline."
                        numericErrorCode: int = 51024
                        originatingService: str = "party"

                    class user_operation_forbidden(EpicException):
                        """
                        docstring
                        """
                        errorMessage: str = "message"
                        numericErrorCode: int = 0
                        originatingService: str = "party"
                        statusCode: int = 400

                class repolink:
                    """
                    docstring
                    """

                    class not_found:
                        """
                        docstring
                        """

                        class repo_not_found(EpicException):
                            """
                            docstring
                            """
                            errorMessage: str = "message"
                            numericErrorCode: int = 0
                            originatingService: str = "party"
                            statusCode: int = 400

            class unauthorized(EpicException):
                """
                docstring
                """
                errorMessage: str = "message"
                numericErrorCode: int = 0
                originatingService: str = "WEX"
                statusCode: int = 400

            class unknown_error(EpicException):
                """
                An unknown error has occurred
                """
                errorMessage: str = "An unknown server error has occurred. Please report to admin."
                intent: str = None

                class v2(EpicException):
                    """
                    An unknown error has occurred
                    """
                    errorMessage: str = "An unknown server error has occurred. Please report to admin."
                    intent: str = None

            class unsupported_media_type(EpicException):
                """
                docstring
                """
                errorMessage: str = "message"
                numericErrorCode: int = 0
                originatingService: str = "WEX"
                statusCode: int = 400

            class validation:
                """
                docstring
                """

                class validation_failed(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Validation Failed. Invalid fields were {0}"
                    numericErrorCode: int = 1040
                    validationFailures: dict = {}

            class world_explorers:
                """
                Parent class for all WEX errors
                """

                class bad_request(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Does not meet minimum requirements."
                    numericErrorCode: int = 92014
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class banned_access_found_when_granting(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Client requested access grant but has banned access entitlement."
                    numericErrorCode: int = 16156
                    originatingService: str = "WEX"

                class friend_limit_exceeded(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "You've exceeded your friend limit."
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class invalid_friend(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Unable load level due to missing Friend Commander, perhaps they unfriended " \
                                        "you?"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class level_in_progress(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "You already have another level in progress."
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class level_not_found(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Mcp does not recognize this level."
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class level_requirements_not_met(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "You do not meet the requirements to play this level."
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class login_reward_not_available(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "{0} day login reward not available until {1}"
                    numericErrorCode: int = 92030
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class manifest_out_of_date(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "A content update is required before starting a mew level. May we apply it " \
                                        "meow?"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class no_matchmaking_id(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Opponent has not joined matchmaking yet"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class not_enough_energy(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "You do not have enough energy to play this level."
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class not_found(EpicException):
                    """
                    docstring
                    """
                    # We're sorry, but we were unable to sell your item as it was not found in your inventory.
                    errorMessage: str = "Sorry, we were unable to find any friends with that search criteria"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class over_hero_limit(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "You have too many heroes in your inventory. Please remove some before " \
                                        "attempting to play this level."
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class purchase_limit_exceeded(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Unable to purchase {0} x +{1} limit increase. This would exceed the max of {2}"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class service_not_required(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "Already joined matchmaking."
                    numericErrorCode: int = 92006
                    originatingService: str = "WEX"

            class xmpp:
                """
                docstring
                """

                class connection(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class server_error(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400

                class timeout(EpicException):
                    """
                    docstring
                    """
                    errorMessage: str = "message"
                    numericErrorCode: int = 0
                    originatingService: str = "WEX"
                    statusCode: int = 400


if __name__ == "__main__":
    try:
        raise errors.com.epicgames.unknown_error.v2("hi")
    except EpicException as e:
        print(e.as_dict())
