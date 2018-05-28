"""Provides the HTTP request handling interface."""

from .const import TIMEOUT
import requests


class Requestor(object):
    """Requestor provides an interface to HTTP requests."""

    def __init__(self):
        """Create an instance of the Requestor class."""
        self._http = requests.Session()

    def close(self):
        """Call close on the underlying session."""
        return self._http.close()

    def get_json(self, url, params=None):
        """Get the JSON responste of a HTTP request."""
        return self._http.get(url, params=params, timeout=TIMEOUT).json()
