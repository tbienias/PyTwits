""" Provide the StockTwits class. """

from .classes import Cursor, Entities, Message, User, Source, Symbol, Watchlist
from .const import (ACCOUNT_API_PATH, BLOCKS_API_PATH, FRIENDSHIPS_API_PATH,
                    GRAPH_API_PATH, MESSAGES_API_PATH, MUTES_API_PATH,
                    SEARCH_API_PATH, STREAMS_API_PATH, WATCHLISTS_API_PATH,
                    BASE_URL)
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
                               'entities': Entities,
                               'message': Message,
                               'messages': self.__message_list_helper,
                               'parent': Message,
                               'results': self.__result_list_helper,
                               'source': Source,
                               'symbol': Symbol,
                               'symbols': self.__symbol_list_helper,
                               'user': User,
                               'users': self.__user_list_helper,
                               'watchlist': Watchlist,
                               'watchlists': self.__watchlist_list_helper}

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

    def __symbol_list_helper(self, json_symbols):
        """Helper for dealing with lists of symbols."""
        symbols = []
        for symbol in json_symbols:
            symbols.append(Message(**symbol))
        return symbols

    def __user_list_helper(self, json_users):
        """Helper for dealing with lists of users."""
        users = []
        for user in json_users:
            users.append(User(**user))
        return users

    def __watchlist_list_helper(self, json_watchlists):
        """Helper for dealing with lists of watchlists."""
        watchlists = []
        for watchlist in json_watchlists:
            watchlists.append(Watchlist(**watchlist))
        return watchlists

    def __query_helper(self, api_path, kwargs, api_extensions=None):
        """Helper which is basically used by every public interface function
        doing all the internal magic."""
        api_path_extended = api_path.path
        if api_extensions is not None:
            api_path_extended = api_path_extended.format(**api_extensions)
        url = BASE_URL.format(api_path_extended)

        kwargs['access_token'] = self.__access_token
        if 'GET' == api_path.request_type:
            json_response = self.__requestor.get_json(url, kwargs)
        elif 'POST' == api_path.request_type:
            json_response = self.__requestor.post_json(url, kwargs)
        for key in ['response', 'errors']:
            json_response.pop(key, None)

        json_objects = []
        for key in json_response:
            if isinstance(json_response[key], list):
                json_objects.append(
                    self.__JSON_OBJECTS[key](json_response[key]))
            else:
                json_objects.append(
                    self.__JSON_OBJECTS[key](**json_response[key]))

        if len(json_objects) == 1:
            return json_objects[0]

        return json_objects

    def streams(self, path, *args, **kwargs):
        """This function provides all the stream functionality offered by the
        StockTwits API."""
        if path not in STREAMS_API_PATH:
            raise InvalidInvocation()
        api_path = STREAMS_API_PATH[path]
        p = {key: kwargs[key] for key in kwargs.keys() & {'id', 'sector_path'}}
        all(map(kwargs.pop, p))  # Remove id and sector_path from kwargs
        return self.__query_helper(api_path, kwargs, p)

    def search(self, path, *args, **kwargs):
        """This function provides all the search functionality offered by the
        StockTwits API."""
        if path not in SEARCH_API_PATH:
            raise InvalidInvocation()
        api_path = SEARCH_API_PATH[path]
        return self.__query_helper(api_path, kwargs)

    def messages(self, path, *args, **kwargs):
        """This function provides all the messaging functionality offered by
        the StockTwits API."""
        if path not in MESSAGES_API_PATH:
            raise InvalidInvocation()
        api_path = MESSAGES_API_PATH[path]
        if "{id}" in api_path.path:
            p = {key: kwargs[key] for key in kwargs.keys() & {'id'}}
            all(map(kwargs.pop, p))  # Remove id from kwargs
        else:
            p = None
        return self.__query_helper(api_path, kwargs, p)

    def graph(self, path, *args, **kwargs):
        """This function provides all the graph functionality offered by
        the StockTwits API."""
        if path not in GRAPH_API_PATH:
            raise InvalidInvocation()
        api_path = GRAPH_API_PATH[path]
        return self.__query_helper(api_path, kwargs)

    def friendships(self, path, *args, **kwargs):
        """This function provides all the friendships functionality
        offered by the StockTwits API."""
        if path not in FRIENDSHIPS_API_PATH:
            raise InvalidInvocation()
        api_path = FRIENDSHIPS_API_PATH[path]
        if "{id}" in api_path.path:
            p = {key: kwargs[key] for key in kwargs.keys() & {'id'}}
            all(map(kwargs.pop, p))  # Remove id from kwargs
        else:
            p = None
        return self.__query_helper(api_path, kwargs, p)

    def watchlists(self, path, *args, **kwargs):
        """This function provides all the watchlists functionality
        offered by the StockTwits API."""
        if path not in WATCHLISTS_API_PATH:
            raise InvalidInvocation()
        api_path = WATCHLISTS_API_PATH[path]
        if "{id}" in api_path.path:
            p = {key: kwargs[key] for key in kwargs.keys() & {'id'}}
            all(map(kwargs.pop, p))  # Remove id from kwargs
        else:
            p = None
        return self.__query_helper(api_path, kwargs, p)

    def blocks(self, path, *args, **kwargs):
        """This function provides all the blocks functionality
        offered by the StockTwits API."""
        if path not in BLOCKS_API_PATH:
            raise InvalidInvocation()
        api_path = BLOCKS_API_PATH[path]
        if "{id}" in api_path.path:
            p = {key: kwargs[key] for key in kwargs.keys() & {'id'}}
            all(map(kwargs.pop, p))  # Remove id from kwargs
        else:
            p = None
        return self.__query_helper(api_path, kwargs, p)

    def mutes(self, path, *args, **kwargs):
        """This function provides all the mutes functionality
        offered by the StockTwits API."""
        if path not in MUTES_API_PATH:
            raise InvalidInvocation()
        api_path = MUTES_API_PATH[path]
        if "{id}" in api_path.path:
            p = {key: kwargs[key] for key in kwargs.keys() & {'id'}}
            all(map(kwargs.pop, p))  # Remove id from kwargs
        else:
            p = None
        return self.__query_helper(api_path, kwargs, p)

    def account(self, path, *args, **kwargs):
        """This function provides all the account functionality
        offered by the StockTwits API."""
        if path not in ACCOUNT_API_PATH:
            raise InvalidInvocation()
        api_path = ACCOUNT_API_PATH[path]
        return self.__query_helper(api_path, kwargs)
