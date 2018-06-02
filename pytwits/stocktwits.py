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

    @staticmethod
    def message_list_helper(json_messages):
        messages = []
        for message in json_messages:
            messages.append(Message(message_attributes=message))
        return messages

    JSON_OBJECTS = {'cursor': Cursor,
                    'message': Message,
                    'messages': message_list_helper.__get__(object),
                    'parent': Message,
                    'symbol': Symbol,
                    'user': User,
                    'watchlist': Watchlist}

    def streams(self, path, *args, **kwargs):
        if path not in API_PATH:
            raise InvalidInvocation()

        p = {key: kwargs[key] for key in kwargs.keys() & {'id', 'sector_path'}}
        api_path = API_PATH[path].format(**p)
        url = BASE_URL.format(api_path)

        all(map(kwargs.pop, p))  # Remove id and sector_path from kwargs
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

    def user(self, id, since=None, max=None, limit=None, filter=None):
        """Wrapper for user function stream.

        Returns messages and the user object.

        :param id: User ID or Username of the stream's user you want to show.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, or videos.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter}

        api_path = API_PATH['user'].format(**{'id': id})
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        user = User(**json_response['user'])
        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return user, cursor, messages

    def symbol(self, id, since=None, max=None, limit=None, filter=None):
        """Wrapper for symbol function stream.

        Returns messages and the symbol object.

        :param id: Ticker symbol, Stock ID, or RIC code of the symbol.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter}

        api_path = API_PATH['symbol'].format(**{'id': id})
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        symbol = Symbol(**json_response['symbol'])
        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return symbol, cursor, messages

    def home(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for home function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter}

        api_path = API_PATH['home']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def friends(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for friends function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['friends']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def mentions(self, since=None, max=None, limit=None):
        """Wrapper for mentions function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        """

        params = {'since': since, 'max': max, 'limit': limit,
                  'access_token': self.access_token}

        api_path = API_PATH['mentions']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def direct(self, since=None, max=None, limit=None):
        """Wrapper for direct function stream.

        Returns direct messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        """

        params = {'since': since, 'max': max, 'limit': limit,
                  'access_token': self.access_token}

        api_path = API_PATH['direct']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def direct_sent(self, since=None, max=None, limit=None):
        """Wrapper for direct_sent function stream.

        Returns direct messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        """

        params = {'since': since, 'max': max, 'limit': limit,
                  'access_token': self.access_token}

        api_path = API_PATH['direct_sent']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def direct_received(self, since=None, max=None, limit=None):
        """Wrapper for direct_sent function stream.

        Returns direct messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        """

        params = {'since': since, 'max': max, 'limit': limit,
                  'access_token': self.access_token}

        api_path = API_PATH['direct_received']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def watchlist(self, id, since=None, max=None, limit=None, filter=None):
        """Wrapper for friends function stream.

        Returns messages.

        :param id: ID of the watch list you want to show from the
        authenticating user.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['watchlist']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        watchlist = Watchlist(**json_response['watchlist'])
        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return watchlist, cursor, messages

    def all(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for all function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['all']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def charts(self, since=None, max=None, limit=None):
        """Wrapper for charts function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['charts']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def equities(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for equities function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['equities']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def forex(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for forex function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['forex']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def futures(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for futures function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['futures']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def private_companies(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for private_companies function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['private_companies']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def suggested(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for suggested function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['suggested']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def symbols(self, symbols, since=None, max=None, limit=None, filter=None):
        """Wrapper for suggested function stream.

        Returns messages.

        :param symbols: List of multiple Ticker symbols or Stock IDs. Max 10.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['symbols']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def trending(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for trending function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['trending']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages

    def sectors(self, since=None, max=None, limit=None, filter=None):
        """Wrapper for sectors function stream.

        Returns messages.

        :param since: Returns results with an ID greater than (more recent
        than) the specified ID.

        :param max: Returns results with an ID less than (older than) or
        equal to the specified ID.

        :param limit: Default and max limit is 30. This limit must be a number
        under 30.

        :param filter: Filter messages by links, charts, videos or top.

        """

        params = {'since': since, 'max': max, 'limit': limit, 'filter': filter,
                  'access_token': self.access_token}

        api_path = API_PATH['sectors']
        url = BASE_URL.format(api_path)
        json_response = self._requestor.get_json(url, params)

        cursor = Cursor(**json_response['cursor'])

        messages = []
        for message in json_response['messages']:
            messages.append(Message(message_attributes=message))

        return cursor, messages