import time
# noinspection PyPackageRequirements
import twitter

from src.config import TIME_BETWEEN_TWEETS
from src.helper import log, env


api = twitter.Api(
    consumer_key=env.get_twitter_consumer_key(),
    consumer_secret=env.get_twitter_consumer_secret(),
    access_token_key=env.get_twitter_access_token_key(),
    access_token_secret=env.get_twitter_access_token_secret()
)


def tweet(message_list):
    """
    Tweet a bunch of messages to Twitter with some time between them.
    :param message_list: Message list.
    :return: All messages tweeted.
    """
    for message in message_list:
        log.info(message)
        api.PostUpdate(message)
        time.sleep(TIME_BETWEEN_TWEETS)
