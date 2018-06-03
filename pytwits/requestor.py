"""Provides the HTTP request handling interface."""

from .const import TIMEOUT
from .exceptions import Forbidden, NotFound, Unauthorized
import requests
from requests.status_codes import codes


class Requestor(object):
    """Requestor provides an interface to HTTP requests."""

    STATUS_EXCEPTIONS = {codes['not_found']: NotFound,
                         codes['unauthorized']: Unauthorized,
                         codes['forbidden']: Forbidden}

    def __init__(self):
        """Create an instance of the Requestor class."""
        self._http = requests.Session()

    def close(self):
        """Call close on the underlying session."""
        return self._http.close()

    def get_json(self, url, params=None):
        """Get the JSON response of a HTTP request."""
        response = self._http.get(url, params=params, timeout=TIMEOUT)
        if response.status_code in self.STATUS_EXCEPTIONS:
            raise self.STATUS_EXCEPTIONS[response.status_code](response)
        return response.json()
