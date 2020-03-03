# Debug
DEBUG = False

# Scheduler
MAX_INSTANCES = 1
GRACE_TIME = 3600

# Data URLs
DATA_ATTEMPTS = 3
DATA_TIMEOUT = 30
DATA_RTD = 15
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)'
URL_BASE = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data'

# Time
TIME_BETWEEN_RESOURCES = 15
TIME_BETWEEN_TWEETS = 300

# Resources
DATA_FOLDER = 'data'
DATA_CONFIRMED = 'Confirmed'
DATA_DEATHS = 'Deaths'
DATA_RECOVERED = 'Recovered'
RESOURCES = [
    {
        'name': DATA_CONFIRMED,
        'data_url': f'{URL_BASE}/csse_covid_19_time_series/time_series_19-covid-{DATA_CONFIRMED}.csv',
        'data_path': f'{DATA_FOLDER}/{DATA_CONFIRMED.lower()}.json',
        'icon': '🟡'
    },
    {
        'name': DATA_DEATHS,
        'data_url': f'{URL_BASE}/csse_covid_19_time_series/time_series_19-covid-{DATA_DEATHS}.csv',
        'data_path': f'{DATA_FOLDER}/{DATA_DEATHS.lower()}.json',
        'icon': '🔴'
    },
    {
        'name': DATA_RECOVERED,
        'data_url': f'{URL_BASE}/csse_covid_19_time_series/time_series_19-covid-{DATA_RECOVERED}.csv',
        'data_path': f'{DATA_FOLDER}/{DATA_RECOVERED.lower()}.json',
        'icon': '🟢'
    }
]
