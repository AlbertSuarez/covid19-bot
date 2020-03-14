import random


# Debug
DEBUG = False

# Scheduler
MAX_INSTANCES = 1
GRACE_TIME = 9 * 60  # 9 minutes

# Time
TIME_BETWEEN_RESOURCES = 15
TIME_BETWEEN_TWEETS = 1 * 60  # 1 minute

# Scrapping
TOR_ENABLE = True
HTTP_PROXY = 'socks5://covid-bot-tor:9050'
SCRAPE_RETRIES_AMOUNT = 10
SCRAPE_RTD_ERROR_MINIMUM = 3
SCRAPE_RTD_ERROR_MAXIMUM = 5

# Resources
DATA_FOLDER = 'data'
DATA_CONFIRMED = 'Confirmed'
DATA_DEATHS = 'Deaths'
DATA_RECOVERED = 'Recovered'
DATA_PATH_DICT = {
    DATA_CONFIRMED: f'{DATA_FOLDER}/{DATA_CONFIRMED.lower()}.json',
    DATA_DEATHS: f'{DATA_FOLDER}/{DATA_DEATHS.lower()}.json',
    DATA_RECOVERED: f'{DATA_FOLDER}/{DATA_RECOVERED.lower()}.json',
}

# Icons
ICON_UP = '⬆️'
ICON_DOWN = '⬇️'
ICON_DICT = {
    DATA_CONFIRMED: '🟡',
    DATA_DEATHS: '🔴',
    DATA_RECOVERED: '🟢'
}

# Resources - Johns Hopkins
JOHNS_HOPKINS_DATA_ATTEMPTS = 3
JOHNS_HOPKINS_DATA_TIMEOUT = 30
JOHNS_HOPKINS_DATA_RTD = 15
JOHNS_HOPKINS_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)'
JOHNS_HOPKINS_URL_BASE = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data'
JOHNS_HOPKINS_RESOURCES = [
    {
        'name': DATA_CONFIRMED,
        'data_url': f'{JOHNS_HOPKINS_URL_BASE}/csse_covid_19_time_series/time_series_19-covid-{DATA_CONFIRMED}.csv',
        'data_path': DATA_PATH_DICT[DATA_CONFIRMED],
        'icon': ICON_DICT[DATA_CONFIRMED]
    },
    {
        'name': DATA_DEATHS,
        'data_url': f'{JOHNS_HOPKINS_URL_BASE}/csse_covid_19_time_series/time_series_19-covid-{DATA_DEATHS}.csv',
        'data_path': DATA_PATH_DICT[DATA_DEATHS],
        'icon': ICON_DICT[DATA_DEATHS]
    },
    {
        'name': DATA_RECOVERED,
        'data_url': f'{JOHNS_HOPKINS_URL_BASE}/csse_covid_19_time_series/time_series_19-covid-{DATA_RECOVERED}.csv',
        'data_path': DATA_PATH_DICT[DATA_RECOVERED],
        'icon': ICON_DICT[DATA_RECOVERED]
    }
]

# Resources - Worldometers
WORLDOMETERS_URL = 'https://www.worldometers.info/coronavirus/'

# Twitter
HASHTAG_LIST = '#coronavirus #covid19'

# Flags
FLAG_DEFAULT = random.choice(['🌍', '🌎', '🌎'])
FLAGS = {
    'China': '🇨🇳',
    'Italy': '🇮🇹',
    'Iran': '🇮🇷',
    'S. Korea': '🇰🇷',
    'Spain': '🇪🇸',
    'Germany': '🇩🇪',
    'France': '🇫🇷',
    'USA': '🇺🇸',
    'Switzerland': '🇨🇭',
    'Norway': '🇳🇴',
    'Sweden': '🇸🇪',
    'Denmark': '🇩🇰',
    'Netherlands': '🇳🇱',
    'UK': '🇬🇧',
    'Japan': '🇯🇵',
    'Diamond Princess': '💎',
    'Belgium': '🇧🇪',
    'Austria': '🇦🇹',
    'Qatar': '🇶🇦',
    'Australia': '🇦🇺',
    'Malaysia': '🇲🇾',
    'Finland': '🇫🇮',
    'Bahrain': '🇧🇭',
    'Canada': '🇨🇦',
    'Singapore': '🇸🇬',
    'Greece': '🇬🇷',
    'Portugal': '🇵🇹',
    'Israel': '🇮🇱',
    'Brazil': '🇧🇷',
    'Czechia': '🇨🇿',
    'Slovenia': '🇸🇮',
    'Hong Kong': '🇭🇰',
    'Iceland': '🇮🇸',
    'Estonia': '🇪🇪',
    'Kuwait': '🇰🇼',
    'Iraq': '🇮🇶',
    'Romania': '🇷🇴',
    'Philippines': '🇵🇭',
    'Indonesia': '🇮🇩',
    'Lebanon': '🇱🇧',
    'Egypt': '🇪🇬',
    'Poland': '🇵🇱',
    'Ireland': '🇮🇪',
    'Saudi Arabia': '🇸🇦',
    'UAE': '🇦🇪',
    'India': '🇮🇳',
    'Thailand': '🇹🇭',
    'San Marino': '🇸🇲',
    'Taiwan': '🇹🇼',
    'Vietnam': '🇻🇳',
    'Luxembourg': '🇱🇺',
    'Russia': '🇷🇺',
    'Chile': '🇨🇱',
    'Serbia': '🇷🇸',
    'Albania': '🇦🇱',
    'Peru': '🇵🇪',
    'Algeria': '🇩🇿',
    'Croatia': '🇭🇷',
    'Brunei': '🇧🇳',
    'Panama': '🇵🇦',
    'Palestine': '🇵🇸',
    'Argentina': '🇦🇷',
    'Slovakia': '🇸🇰',
    'Bulgaria': '🇧🇬',
    'Georgia': '🇬🇪',
    'Pakistan': '🇵🇰',
    'Belarus': '🇧🇾',
    'Ecuador': '🇪🇨',
    'Latvia': '🇱🇻',
    'Costa Rica': '🇨🇷',
    'Hungary': '🇭🇺',
    'South Africa': '🇿🇦',
    'Senegal': '🇸🇳',
    'Cyprus': '🇨🇾',
    'Oman': '🇴🇲',
    'Bosnia and Herzegovina': '🇧🇦',
    'Malta': '🇲🇹',
    'Morocco': '🇲🇦',
    'Tunisia': '🇹🇳',
    'Colombia': '🇨🇴',
    'Azerbaijan': '🇦🇿',
    'Armenia': '🇦🇲',
    'Mexico': '🇲🇽',
    'North Macedonia': '🇲🇰',
    'Dominican Republic': '🇩🇴',
    'Afghanistan': '🇦🇫',
    'Macao': '🇲🇴',
    'Bolivia': '🇧🇴',
    'Maldives': '🇲🇻',
    'Sri Lanka': '🇱🇰',
    'Faeroe Islands': '🇫🇴',
    'Lithuania': '🇱🇹',
    'Jamaica': '🇯🇲',
    'Cambodia': '🇰🇭',
    'New Zealand': '🇳🇿',
    'French Guiana': '🇬🇫',
    'Kazakhstan': '🇰🇿',
    'Martinique': '🇲🇶',
    'Moldova': '🇲🇩',
    'Paraguay': '🇵🇾',
    'Réunion': '🇷🇪',
    'Turkey': '🇹🇷',
    'Cuba': '🇨🇺',
    'Liechtenstein': '🇱🇮',
    'Uruguay': '🇺🇾',
    'Ukraine': '🇺🇦',
    'Bangladesh': '🇧🇩',
    'Channel Islands': '🇯🇪',
    'French Polynesia': '🇵🇫',
    'Puerto Rico': '🇵🇷',
    'Monaco': '🇲🇨',
    'Nigeria': '🇳🇬',
    'Aruba': '🇦🇼',
    'Burkina Faso': '🇧🇫',
    'Cameroon': '🇨🇲',
    'DRC': '🇨🇩',
    'Ghana': '🇬🇭',
    'Honduras': '🇭🇳',
    'Namibia': '🇳🇦',
    'Saint Martin': '🇲🇶',
    'Trinidad and Tobago': '🇹🇹',
    'Venezuela': '🇻🇪',
    'Guyana': '🇬🇾',
    'Sudan': '🇸🇩',
    'Andorra': '🇦🇩',
    'Jordan': '🇯🇴',
    'Nepal': '🇳🇵',
    'Antigua and Barbuda': '🇦🇬',
    'Bhutan': '🇧🇹',
    'Cayman Islands': '🇰🇾',
    'Ivory Coast': '🇨🇮',
    'Curaçao': '🇨🇼',
    'Ethiopia': '🇪🇹',
    'Gabon': '🇬🇦',
    'Gibraltar': '🇬🇮',
    'Guadeloupe': '🇬🇵',
    'Guatemala': '🇬🇹',
    'Guinea': '🇬🇳',
    'Vatican City': '🇻🇦',
    'Kenya': '🇰🇪',
    'Mauritania': '🇲🇷',
    'Mongolia': '🇲🇳',
    'Rwanda': '🇷🇼',
    'St. Barth': '🇧🇱',
    'Saint Lucia': '🇱🇨',
    'St. Vincent Grenadines': '🇻🇨',
    'Suriname': '🇸🇷',
    'Eswatini': '🇸🇿',
    'Togo': '🇹🇬',
    'U.S. Virgin Islands': '🇻🇬'
}
