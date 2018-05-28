from collections import namedtuple


User = namedtuple('User', ['id', 'username', 'name', 'avatar_url',
                           'avatar_url_ssl', 'join_date',
                           'official', 'identity',
                           'classification', 'followers',
                           'following', 'ideas',
                           'watchlist_stocks_count', 'like_count'])


Cursor = namedtuple('Cursor', ['more', 'since', 'max'])


class Message(object):

    def __init__(self, *args, **kwargs):
        attributes = kwargs.get('message_attributes')
        self.__dict__.update(attributes)

        # Add attributes, which might be missing
        self.symbols = attributes.get('symbols', [])
        self.conversation = attributes.get('conversation', {})
        self.links = attributes.get('links', [])
        self.reshares = attributes.get('reshares', {})
        self.likes = attributes.get('likes', {})

