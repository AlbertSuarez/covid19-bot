import json
import os
import time

from src.config import RESOURCES, TIME_BETWEEN_RESOURCES
from src.helper import log
from src.johns_hopkins import retriever


def run():
    """
    Main function in order to process a new iteration of the Twitter bot.
    :return: Iteration done.
    """
    for item in RESOURCES:
        item_name = item['name']
        log.info(f'Processing {item_name}...')
        results = retriever.get_last_update(item['data_url'])
        if results is not None:
            item_data_path = item['data_path']
            item_data_path_exists = os.path.isfile(item_data_path)
            with open(item_data_path, 'w') as item_data_file:
                json.dump(results, item_data_file)
        time.sleep(TIME_BETWEEN_RESOURCES)
