

class Cursor(object):

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)


class Message(object):

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

        # Add attributes, which might be missing due to no authentication
        self.symbols = kwargs.get('symbols', [])
        self.conversation = kwargs.get('conversation', {})
        self.links = kwargs.get('links', [])
        self.reshares = kwargs.get('reshares', {})
        self.likes = kwargs.get('likes', {})


class Symbol(object):

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)


class User(object):

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

        # Add attributes, which might be missing due to no authentication
        self.is_blocking = kwargs.get('is_blocking', None)
        self.is_follower = kwargs.get('is_follower', None)
        self.is_following = kwargs.get('is_following', None)
        self.is_muting = kwargs.get('is_muting', None)
        self.is_subscribed = kwargs.get('is_subscribed', None)


class Watchlist(object):

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)
