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

# Resources
DATA_FOLDER = 'data'
RESOURCES = [
    {
        'name': 'Confirmed',
        'data_url': f'{URL_BASE}/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
        'data_path': f'{DATA_FOLDER}/confirmed.json'
    },
    {
        'name': 'Deaths',
        'data_url': f'{URL_BASE}/csse_covid_19_time_series/time_series_19-covid-Deaths.csv',
        'data_path': f'{DATA_FOLDER}/deaths.json'
    },
    {
        'name': 'Recovered',
        'data_url': f'{URL_BASE}/csse_covid_19_time_series/time_series_19-covid-Recovered.csv',
        'data_path': f'{DATA_FOLDER}/recovered.json'
    }
]
