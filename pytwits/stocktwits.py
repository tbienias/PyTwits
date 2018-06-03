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
        self.__access_token = access_token

        self.__requestor = Requestor()
        """ An instance of :class:`.Requestor`.
        Provides the interface for REST-API requests.
        """

        self.__JSON_OBJECTS = {'cursor': Cursor,
                               'message': Message,
                               'messages': self.__message_list_helper,
                               'parent': Message,
                               'results': self.__result_list_helper,
                               'symbol': Symbol,
                               'user': User,
                               'watchlist': Watchlist}

    def __message_list_helper(self, json_messages):
        """Helper for dealing with lists of messages."""
        messages = []
        for message in json_messages:
            messages.append(Message(**message))
        return messages

    def __result_list_helper(self, json_results):
        """Heler for dealing with lists of results."""
        objects = []
        for result in json_results:
            type = result['type']
            del result['type']
            objects.append(self.__JSON_OBJECTS[type](**result))
        return objects

    def __query_helper(self, path, kwargs, api_extensions=None):
        """Helper which is basically used by every public interface function
        doing all the internal magic."""
        if path not in API_PATH:
            raise InvalidInvocation()
        api_path = API_PATH[path]
        if api_extensions is not None:
            api_path = api_path.format(**api_extensions)
        url = BASE_URL.format(api_path)

        kwargs['access_token'] = self.__access_token
        json_response = self.__requestor.get_json(url, kwargs)
        del json_response['response']

        json_objects = []
        for k in json_response:
            if isinstance(json_response[k], list):
                json_objects.append(self.__JSON_OBJECTS[k](json_response[k]))
            else:
                json_objects.append(self.__JSON_OBJECTS[k](**json_response[k]))

        if len(json_objects) == 1:
            return json_objects[0]

        return json_objects

    def streams(self, path, *args, **kwargs):
        """This function provides all the stream functionality offered by the
        StockTwits API."""
        p = {key: kwargs[key] for key in kwargs.keys() & {'id', 'sector_path'}}
        all(map(kwargs.pop, p))  # Remove id and sector_path from kwargs
        return self.__query_helper(path, kwargs, p)

    def search(self, path, *args, **kwargs):
        """This function provides all the search functionality offered by the
        StockTwits API."""
        return self.__query_helper(path, kwargs)
