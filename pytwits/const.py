""" stocktwits constants. """

import os


__version__ = '0.1'

API_PATH = {
    'authorize':    'api/2/oauth/authorize',
    'token':        'api/2/oauth/token',
    'user':         'api/2/streams/user/{id}.json'
}

BASE_URL = 'https://api.stocktwits.com/{}'

TIMEOUT = float(os.environ.get('pytwits_timeout', 16))
