""" stocktwits constants. """

import os


__version__ = '0.1'

API_PATH = {

    # Streams API paths
    'authorize':            'api/2/oauth/authorize',
    'token':                'api/2/oauth/token',
    'user':                 'api/2/streams/user/{id}.json',
    'symbol':               'api/2/streams/symbol/{id}.json',
    'home':                 'api/2/streams/home.json',
    'friends':              'api/2/streams/friends.json',
    'mentions':             'api/2/streams/mentions.json',
    'direct':               'api/2/streams/direct.json',
    'direct_sent':          'api/2/streams/direct_sent.json',
    'direct_received':      'api/2/streams/direct_received.json',
    'watchlist':            'api/2/streams/watchlist/{id}.json',
    'all':                  'api/2/streams/all.json',
    'charts':               'api/2/streams/charts.json',
    'equities':             'api/2/streams/equities.json',
    'forex':                'api/2/streams/forex.json',
    'futures':              'api/2/streams/futures.json',
    'private_companies':    'api/2/streams/direct.json',
    'suggested':            'api/2/streams/suggested.json',
    'symbols':              'api/2/streams/symbols.json',
    'trending':             'api/2/streams/trending.json',
    'sectors':              'api/2/streams/sectors/{sector_path}.json',
    'conversation':         'api/2/streams/conversation/{id}.json',

    # Search API paths
    'search':               'api/2/search.json',
    'search/symbols':       'api/2/search/symbols.json',
    'search/users':         'api/2/search/users.json',

    # Messags API paths
    'create':               'api/2/messages/create.json',
    'show':                 'api/2/messages/show/{id}.json',
    'like':                 'api/2/messages/like.json',
    'unlike':               'api/2/messages/unlike.json'
}

BASE_URL = 'https://api.stocktwits.com/{}'

HTTP_REQUEST = {

    # Streams HTTP requests
    'authorize':            'GET',
    'token':                'GET',
    'user':                 'GET',
    'symbol':               'GET',
    'home':                 'GET',
    'friends':              'GET',
    'mentions':             'GET',
    'direct':               'GET',
    'direct_sent':          'GET',
    'direct_received':      'GET',
    'watchlist':            'GET',
    'all':                  'GET',
    'charts':               'GET',
    'equities':             'GET',
    'forex':                'GET',
    'futures':              'GET',
    'private_companies':    'GET',
    'suggested':            'GET',
    'symbols':              'GET',
    'trending':             'GET',
    'sectors':              'GET',
    'conversation':         'GET',

    # Search HTTP requests
    'search':               'GET',
    'search/symbols':       'GET',
    'search/users':         'GET',

    # Messags HTTP requests
    'create':               'POST',
    'show':                 'GET',
    'like':                 'POST',
    'unlike':               'POST'
}

TIMEOUT = float(os.environ.get('pytwits_timeout', 16))
