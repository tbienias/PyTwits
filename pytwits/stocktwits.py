""" Provide the StockTwits class. """

from .classes import Cursor, Message, User, Symbol, Watchlist
from .const import API_PATH, BASE_URL
from .exceptions import InvalidInvocation
from .requestor import Requestor


class StockTwits(object):
    """The StockTwits class provides convenient access to StockTwits' API.

    Instances of this class are the gateway to interacting with StockTwits' API
    through pytwits. The canonical way to obtain an instance of this class is
    via:

    .. code-block:: python

       import pytwits
       stocktwits = pytwits.StockTwits(access_token='TOKEN')

    """

    def __init__(self, access_token=None):
        """Create an instance of the StockTwits class."""
        self.access_token = access_token

        self._requestor = Requestor()
        """ An instance of :class:`.Requestor`.
        Provides the interface for REST-API requests.
        """

        self.JSON_OBJECTS = {'cursor': Cursor,
                             'message': Message,
                             'messages': self.message_list_helper,
                             'parent': Message,
                             # 'results': self.result_list_helper,
                             'symbol': Symbol,
                             'user': User,
                             'watchlist': Watchlist}

    def message_list_helper(self, json_messages):
        messages = []
        for message in json_messages:
            messages.append(Message(message_attributes=message))
        return messages

    def query_helper(self, path, api_extensions, kwargs):

        if path not in API_PATH:
            raise InvalidInvocation()

        api_path = API_PATH[path].format(**api_extensions)
        url = BASE_URL.format(api_path)

        kwargs['access_token'] = self.access_token
        json_response = self._requestor.get_json(url, kwargs)
        del json_response['response']

        json_objects = []
        for k in json_response:
            if isinstance(json_response[k], list):
                json_objects.append(self.JSON_OBJECTS[k](json_response[k]))
            else:
                json_objects.append(self.JSON_OBJECTS[k](**json_response[k]))

        return json_objects

    def streams(self, path, *args, **kwargs):

        p = {key: kwargs[key] for key in kwargs.keys() & {'id', 'sector_path'}}
        all(map(kwargs.pop, p))  # Remove id and sector_path from kwargs
        return self.query_helper(path, p, kwargs)
