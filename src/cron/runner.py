import json
import os
import time

import dictdiffer

from src.config import TIME_BETWEEN_RESOURCES, DATA_CONFIRMED, DATA_DEATHS, DATA_RECOVERED, FLAGS, \
    FLAG_DEFAULT, HASHTAG_LIST, ICON_UP, ICON_DOWN, DATA_PATH_DICT, ICON_DICT
from src.helper import log
from src.worldometers import retriever
from src.twitter import api


def _notify_changes(diff_tuple, resource_type, icon, results, total_worldwide):
    """
    Generate sentence notifying the change and publishing to Twitter.
    :param diff_tuple: Changes tuple.
    :param resource_type: Type of resource.
    :param icon: Icon to add at the beginning of the message.
    :param results: All results updated.
    :param total_worldwide: Amount of total cases before notifying it.
    :return: Changes notified and total worldwide updated.
    """
    message_list = list()
    if diff_tuple[0] == 'change':
        number = diff_tuple[2][0] - diff_tuple[2][1]
        place = diff_tuple[1]
        place = place if type(place) is not list else place[0]
        total = results[place]
        flag = FLAGS.get(place, FLAG_DEFAULT)
        place_h = '#{}'.format(''.join([c.lower().capitalize() for c in place.strip().split()]))
        total_worldwide += number
        if number > 0:
            if resource_type == DATA_CONFIRMED:
                message_list.append(
                    f'{icon} {ICON_UP}  {abs(number):,} new confirmed case(s) in {place} {flag}  totaling {total:,} '
                    f'in this place. Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}')
            elif resource_type == DATA_DEATHS:
                message_list.append(
                    f'{icon} {ICON_UP}  {abs(number):,} new death(s) confirmed in {place} {flag}  totaling {total:,} '
                    f'in this place. Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}'
                )
            elif resource_type == DATA_RECOVERED:
                message_list.append(
                    f'{icon} {ICON_UP}  {abs(number):,} new recoveries in {place} {flag}  totaling {total:,} '
                    f'in this place. Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}'
                )
        elif number < 0:
            if resource_type == DATA_CONFIRMED:
                message_list.append(
                    f'{icon} {ICON_DOWN}  Confirmed cases have decreased in {abs(number):,} in {place} {flag}  '
                    f'totaling {total:,} in this place. Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}'
                )
            elif resource_type == DATA_DEATHS:
                message_list.append(
                    f'{icon} {ICON_DOWN}  Deaths have decreased in {abs(number):,} in {place} {flag}  '
                    f'totaling {total:,} in this place. Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}'
                )
            elif resource_type == DATA_RECOVERED:
                message_list.append(
                    f'{icon} {ICON_DOWN}  Recovered cases have decreased in {abs(number):,} in {place} {flag}  '
                    f'totaling {total:,} in this place. Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}'
                )
    elif diff_tuple[0] == 'add':
        for place, number in diff_tuple[2]:
            if number > 0:
                total_worldwide += number
                place = place if type(place) is not list else place[0]
                flag = FLAGS.get(place, FLAG_DEFAULT)
                place_h = '#{}'.format(''.join([c.lower().capitalize() for c in place.strip().split()]))
                if resource_type == DATA_CONFIRMED:
                    message_list.append(
                        f'{icon} {ICON_UP}  First {number:,} confirmed case(s) in {place} {flag}. '
                        f'Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}'
                    )
                elif resource_type == DATA_DEATHS:
                    message_list.append(
                        f'{icon} {ICON_UP}  First {number:,} death(s) in {place} {flag}. '
                        f'Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}'
                    )
                elif resource_type == DATA_RECOVERED:
                    message_list.append(
                        f'{icon} {ICON_UP}  First {number:,} recovered case(s) in {place} {flag}. '
                        f'Already {total_worldwide:,} worldwide. {HASHTAG_LIST} {place_h}'
                    )
    api.tweet(message_list)
    return total_worldwide


def run():
    """
    Main function in order to process a new iteration of the Twitter bot.
    :return: Iteration done.
    """
    try:
        resources_list = [DATA_CONFIRMED, DATA_DEATHS, DATA_RECOVERED]
        confirmed_results, deaths_results, recovered_results = retriever.get_last_update()
        for i, item_name in enumerate(resources_list):
            log.info(f'{i + 1}/{len(resources_list)} Processing {item_name}...')
            # Get results
            results = None
            if item_name == DATA_CONFIRMED:
                results = confirmed_results
            elif item_name == DATA_DEATHS:
                results = deaths_results
            elif item_name == DATA_RECOVERED:
                results = recovered_results
            # Process
            if results is not None:
                item_data_path = DATA_PATH_DICT[item_name]
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
                    total_worldwide = sum(old_results.values())
                    diff_results = list(dictdiffer.diff(results, old_results))
                    for j, diff_tuple in enumerate(diff_results):
                        log.info(f'{j + 1}/{len(diff_results)} New changes found: [{diff_tuple}]')
                        total_worldwide = _notify_changes(
                            diff_tuple, item_name, ICON_DICT[item_name], results, total_worldwide
                        )
            time.sleep(TIME_BETWEEN_RESOURCES)
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
