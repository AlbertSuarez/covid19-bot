import time

from src.config import TIME_BETWEEN_TWEETS
from src.helper import log


def tweet(message_list):
    """
    Tweet a bunch of messages to Twitter with some time between them.
    :param message_list: Message list.
    :return: All messages tweeted.
    """
    for message in message_list:
        log.info(message)
        time.sleep(TIME_BETWEEN_TWEETS)
