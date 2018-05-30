"""Provide exception classes for the pytiwts package."""


class PytwitsException(Exception):
    """Base exception class for exceptions that occur within this package."""


class ResponseException(PytwitsException):
    """Indicate that there was an error with the completed HTTP request."""

    def __init__(self, response):
        """Initialize a ResponseException instance.

        :param response: A requests.response instance.

        """
        self.response = response
        super(ResponseException, self).__init__('received {} HTTP response'
                                                .format(response.status_code))


class Forbidden(ResponseException):
    """Indicate the authentication is not permitted for the request."""


class NotFound(ResponseException):
    """Indicate that the requested URL was not found."""


class Unauthorized(ResponseException):
    """Indicate that the request used an invalid access token or none at
    all."""
