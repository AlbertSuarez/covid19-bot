import os


def _get(env_key):
    if env_key in os.environ:
        return os.environ[env_key]
    return None


def get_twitter_consumer_key():
    """
    Retrieve the Twitter consumer key as a environment variable.
    :return: Environment variable.
    """
    return _get('TWITTER_CONSUMER_KEY')


def get_twitter_consumer_secret():
    """
    Retrieve the Twitter consumer secret as a environment variable.
    :return: Environment variable.
    """
    return _get('TWITTER_CONSUMER_SECRET')


def get_twitter_access_token_key():
    """
    Retrieve the Twitter access token key as a environment variable.
    :return: Environment variable.
    """
    return _get('TWITTER_ACCESS_TOKEN_KEY')


def get_twitter_access_token_secret():
    """
    Retrieve the Twitter access token secret as a environment variable.
    :return: Environment variable.
    """
    return _get('TWITTER_ACCESS_TOKEN_SECRET')
