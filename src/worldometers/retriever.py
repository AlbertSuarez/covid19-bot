import random
import time
import requests
import telnetlib

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from src.config import SCRAPE_RETRIES_AMOUNT, SCRAPE_RTD_ERROR_MINIMUM, SCRAPE_RTD_ERROR_MAXIMUM, \
    WORLDOMETERS_URL, TOR_ENABLE, IP_ECHO_ENDPOINT, HTTP_PROXY
from src.helper import log


def __get_ip():
    return requests.get(IP_ECHO_ENDPOINT, proxies={'http': HTTP_PROXY}).text


def __request_ip_change():
    tn = telnetlib.Telnet('covid19-bot-tor', 9051)
    tn.read_until("Escape character is '^]'.", 2)
    tn.write('AUTHENTICATE ""\r\n')
    tn.read_until('250 OK', 2)
    tn.write('signal NEWNYM\r\n')
    tn.read_until('250 OK', 2)
    tn.write('quit\r\n')
    tn.close()


def __wait_for_ip_confirmation(ip_address):
    while True:
        new_ip_address = __get_ip()
        if new_ip_address == ip_address:
            time.sleep(1)
        else:
            log.info(f'New IP address allocated: [{new_ip_address}]')
            break


def _get_html(url):
    """
    Retrieves the HTML content given a Internet accessible URL.
    :param url: URL to retrieve.
    :return: HTML content formatted as String, None if there was an error.
    """
    if TOR_ENABLE:
        ip_address = __get_ip()
        log.info(f'Current IP address: [{ip_address}]')
        __request_ip_change()
        __wait_for_ip_confirmation(ip_address)
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
        table_countries = soup.findChildren('table', id='main_table_countries')
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
