import csv
import time
import requests

from io import StringIO

from src.config import JOHNS_HOPKINS_USER_AGENT, JOHNS_HOPKINS_DATA_ATTEMPTS, JOHNS_HOPKINS_DATA_TIMEOUT, JOHNS_HOPKINS_DATA_RTD
from src.helper import log


def get_last_update(data_url):
    """
    Retrieve data from Johns Hopinks CSV files given a accessible URL.
    :param data_url: Data URL.
    :return: Dictionary with the last update grouped by location.
    """
    result_dict = dict()
    for attempt in range(JOHNS_HOPKINS_DATA_ATTEMPTS):
        try:
            response = requests.get(data_url, headers={'User-Agent': JOHNS_HOPKINS_USER_AGENT}, timeout=JOHNS_HOPKINS_DATA_TIMEOUT)
            rows = [row for row in csv.reader(StringIO(response.text), delimiter=',')][1:]
            for row in rows:
                dict_key = row[1] if not row[0] else f'{row[0]}, {row[1]}'
                result_dict[dict_key] = int(row[-1])
            return result_dict
        except Exception as e:
            log.error(f'Cannot retrieve information from {data_url} - Attempt [{attempt + 1}] - [{e}]')
            time.sleep(JOHNS_HOPKINS_DATA_RTD)
            if attempt == JOHNS_HOPKINS_DATA_ATTEMPTS - 1:
                log.exception(e)
                return None
