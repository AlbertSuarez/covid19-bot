import json
import os
import time

import dictdiffer

from src.config import RESOURCES, TIME_BETWEEN_RESOURCES, DATA_CONFIRMED, DATA_DEATHS, DATA_RECOVERED
from src.helper import log
from src.johns_hopkins import retriever
from src.twitter import api


def _notify_changes(diff_tuple, resource_type, icon, results):
    """
    Generate sentence notifying the change and publishing to Twitter.
    :param diff_tuple: Changes tuple.
    :param resource_type: Type of resource.
    :param icon: Icon to add at the beginning of the message.
    :param results: All results updated.
    :return: Changes notified.
    """
    message_list = list()
    if diff_tuple[0] == 'change':
        change_diff = diff_tuple[2][0] - diff_tuple[2][1]
        change_place = diff_tuple[1]
        if change_diff > 0:
            if resource_type == DATA_CONFIRMED:
                message_list.append(f'{icon} {change_diff} new confirmed cases in {change_place}.')
            elif resource_type == DATA_DEATHS:
                message_list.append(f'{icon} {change_diff} new deaths confirmed in {change_place}.')
            elif resource_type == DATA_RECOVERED:
                message_list.append(f'{icon} {change_diff} could recover in {change_place}.')
        elif change_diff < 0:
            if resource_type == DATA_CONFIRMED:
                message_list.append(f'{icon} Confirmed cases have decreased in {change_diff} in {change_place}.')
            elif resource_type == DATA_DEATHS:
                message_list.append(f'{icon} Deaths have decreased in {change_diff} in {change_place}.')
            elif resource_type == DATA_RECOVERED:
                message_list.append(f'{icon} Recovered scenarios have decreased in {change_diff} in {change_place}.')
    elif diff_tuple[0] == 'add':
        for place, number in diff_tuple[2]:
            if number > 0:
                if resource_type == DATA_CONFIRMED:
                    message_list.append(f'{icon} First {number} confirmed cases in {place}.')
                elif resource_type == DATA_DEATHS:
                    message_list.append(f'{icon} First {number} deaths in {place}.')
                elif resource_type == DATA_RECOVERED:
                    message_list.append(f'{icon} First {number} recovered cases in {place}.')
    api.tweet(message_list)


def run():
    """
    Main function in order to process a new iteration of the Twitter bot.
    :return: Iteration done.
    """
    try:
        for i, item in enumerate(RESOURCES):
            item_name = item['name']
            log.info(f'{i + 1}/{len(RESOURCES)} Processing {item_name}...')
            results = retriever.get_last_update(item['data_url'])
            if results is not None:
                item_data_path = item['data_path']
                item_data_path_exists = os.path.isfile(item_data_path)
                # Get old results if they exist
                old_results = dict()
                if item_data_path_exists:
                    with open(item_data_path, 'r') as item_data_file:
                        old_results = json.load(item_data_file)
                # Save latest results
                with open(item_data_path, 'w') as item_data_file:
                    json.dump(results, item_data_file)
                # Check for differences if it did not exist before
                if item_data_path_exists:
                    diff_results = list(dictdiffer.diff(results, old_results))
                    for j, diff_tuple in enumerate(diff_results):
                        log.info(f'{j + 1}/{len(diff_results)} New changes found: [{diff_tuple}]')
                        _notify_changes(diff_tuple, item_name, item['icon'], results)
            time.sleep(TIME_BETWEEN_RESOURCES)
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
