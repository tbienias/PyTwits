""" Provide the StockTwits class. """

from .classes import Cursor, Message, User
from .const import API_PATH, BASE_URL
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
