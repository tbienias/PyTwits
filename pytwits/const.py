""" stocktwits constants. """

# Disable E501 for api paths
# TODO: Outsource this to a flake8 config file or so
# flake8: noqa

import os


__version__ = '0.1'


class APIPath:

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)


STREAMS_API_PATH = {

    'authorize':         APIPath(path='api/2/oauth/authorize', request_type='GET'),
    'token':             APIPath(path='api/2/oauth/token', request_type='GET'),
    'user':              APIPath(path='api/2/streams/user/{id}.json', request_type='GET'),
    'symbol':            APIPath(path='api/2/streams/symbol/{id}.json', request_type='GET'),
    'home':              APIPath(path='api/2/streams/home.json', request_type='GET'),
    'friends':           APIPath(path='api/2/streams/friends.json', request_type='GET'),
    'mentions':          APIPath(path='api/2/streams/mentions.json', request_type='GET'),
    'direct':            APIPath(path='api/2/streams/direct.json', request_type='GET'),
    'direct_sent':       APIPath(path='api/2/streams/direct_sent.json', request_type='GET'),
    'direct_received':   APIPath(path='api/2/streams/direct_received.json', request_type='GET'),
    'watchlist':         APIPath(path='api/2/streams/watchlist/{id}.json', request_type='GET'),
    'all':               APIPath(path='api/2/streams/all.json', request_type='GET'),
    'charts':            APIPath(path='api/2/streams/charts.json', request_type='GET'),
    'forex':             APIPath(path='api/2/streams/forex.json', request_type='GET'),
    'equities':          APIPath(path='api/2/streams/equities.json', request_type='GET'),
    'futures':           APIPath(path='api/2/streams/futures.json', request_type='GET'),
    'private_companies': APIPath(path='api/2/streams/direct.json', request_type='GET'),
    'suggested':         APIPath(path='api/2/streams/suggested.json', request_type='GET'),
    'symbols':           APIPath(path='api/2/streams/symbols.json', request_type='GET'),
    'trending':          APIPath(path='api/2/streams/trending.json', request_type='GET'),
    'sectors':           APIPath(path='api/2/streams/sectors/{sector_path}.json', request_type='GET'),
    'conversation':      APIPath(path='api/2/streams/conversation/{id}.json', request_type='GET'),
}

SEARCH_API_PATH = {

    'search':            APIPath(path='api/2/search.json', request_type='GET'),
    'search/symbols':    APIPath(path='api/2/search/symbols.json', request_type='GET'),
    'search/users':      APIPath(path='api/2/search/users.json', request_type='GET'),
}

MESSAGES_API_PATH = {

    'create':            APIPath(path='api/2/messages/create.json', request_type='POST'),
    'show':              APIPath(path='api/2/messages/show/{id}.json', request_type='GET'),
    'like':              APIPath(path='api/2/messages/like.json', request_type='POST'),
    'unlike':            APIPath(path='api/2/messages/unlike.json', request_type='POST'),
}

GRAPH_API_PATH = {

    'blocking':          APIPath(path='api/2/graph/blocking.json', request_type='GET'),
    'muting':            APIPath(path='api/2/graph/muting.json', request_type='GET'),
    'following':         APIPath(path='api/2/graph/following.json', request_type='GET'),
    'followers':         APIPath(path='api/2/graph/followers.json', request_type='GET'),
    'symbols':           APIPath(path='api/2/graph/symbols.json', request_type='GET'),
}

FRIENDSHIPS_API_PATH = {

    'create':            APIPath(path='api/2/friendships/create/{id}.json', request_type='POST'),
    'destroy':           APIPath(path='api/2/friendships/destroy/{id}.json', request_type='POST'),
}

WATCHLISTS_API_PATH = {

    'watchlists':        APIPath(path='api/2/watchlists.json', request_type='GET'),
    'create':            APIPath(path='api/2/watchlists/create.json', request_type='POST'),
    'update':            APIPath(path='api/2/watchlists/update/{id}.json', request_type='POST'),
    'destroy':           APIPath(path='api/2/watchlists/destroy/{id}.json', request_type='POST'),
    'show':              APIPath(path='api/2/watchlists/show/{id}.json', request_type='GET'),
    'symbols/create':    APIPath(path='api/2/watchlists/{id}/symbols/create.json', request_type='POST'),
    'symbols/destroy':   APIPath(path='api/2/watchlists/{id}/symbols/destroy.json', request_type='POST'),
}

BLOCKS_API_PATH = {

    'create':            APIPath(path='api/2/blocks/create/{id}.json', request_type='POST'),
    'destroy':           APIPath(path='api/2/blocks/destroy/{id}.json', request_type='POST')
}

MUTES_API_PATH = {

    'create':            APIPath(path='api/2/mutes/create/{id}.json', request_type='POST'),
    'destroy':           APIPath(path='api/2/mutes/destroy/{id}.json', request_type='POST')
}

ACCOUNT_API_PATH = {

    'verify':            APIPath(path='api/2/account/verify.json', request_type='GET'),
    'update':            APIPath(path='api/2/account/update.json', request_type='POST')
}

BASE_URL = 'https://api.stocktwits.com/{}'

TIMEOUT = float(os.environ.get('pytwits_timeout', 16))
