import random
import time
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from src.config import SCRAPE_RETRIES_AMOUNT, SCRAPE_RTD_ERROR_MINIMUM, SCRAPE_RTD_ERROR_MAXIMUM, \
    WORLDOMETERS_URL, TOR_ENABLE, HTTP_PROXY
from src.helper import log


def _get_html(url):
    """
    Retrieves the HTML content given a Internet accessible URL.
    :param url: URL to retrieve.
    :return: HTML content formatted as String, None if there was an error.
    """
    for i in range(0, SCRAPE_RETRIES_AMOUNT):
        try:
            proxies = {'http': HTTP_PROXY} if TOR_ENABLE else {}
            headers = {'User-Agent': UserAgent().random}
            response = requests.get(url, proxies=proxies, headers=headers)
            assert response.ok
            html_content = response.content
            return html_content
        except Exception as e:
            if i == SCRAPE_RETRIES_AMOUNT - 1:
                log.error(f'Unable to retrieve HTML from {url}: {e}')
            else:
                log.warn(f'Unable to retrieve HTML from {url} - Retry {i}: {e}')
                time.sleep(random.uniform(SCRAPE_RTD_ERROR_MINIMUM, SCRAPE_RTD_ERROR_MAXIMUM))
    return None


def get_last_update():
    """
    Retrieve data from Worldometers.
    :return: 3 Dictionaries (confirmed, deaths & recovered) with the last update grouped by location.
    """
    confirmed_dict = dict()
    death_dict = dict()
    recovered_dict = dict()
    html_content = _get_html(WORLDOMETERS_URL)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        table_countries = soup.findChildren('table', id='main_table_countries_today')
        # Table
        if table_countries:
            body_list = table_countries[0].findChildren('tbody')
            # Body
            if body_list:
                row_list = body_list[0].findChildren('tr')
                # Rows
                if row_list:
                    for row in row_list:
                        # Every row
                        try:
                            cell_list = row.findChildren('td')
                            if cell_list and len(cell_list) >= 6:
                                # Extract country
                                country_cell = cell_list[0]
                                if country_cell.find('a'):
                                    country = cell_list[0].find('a').text.strip()
                                else:
                                    country = cell_list[0].text.strip()
                                # Extract string
                                confirmed_n = '' if not cell_list[1] else cell_list[1].text.strip().replace(',', '')
                                deaths_n = '' if not cell_list[3] else cell_list[3].text.strip().replace(',', '')
                                recovered_n = '' if not cell_list[5] else cell_list[5].text.strip().replace(',', '')
                                # Parse to integer
                                confirmed_n = 0 if not confirmed_n else int(confirmed_n)
                                deaths_n = 0 if not deaths_n else int(deaths_n)
                                recovered_n = 0 if not recovered_n else int(recovered_n)
                                # Add to dictionary
                                confirmed_dict[country] = confirmed_n
                                death_dict[country] = deaths_n
                                recovered_dict[country] = recovered_n
                        except Exception as e:
                            log.warn(f'There was an error processing one row - [{e}]. Ignoring...')
    return confirmed_dict, death_dict, recovered_dict
