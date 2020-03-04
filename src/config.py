import random


# Debug
DEBUG = False

# Scheduler
MAX_INSTANCES = 1
GRACE_TIME = 1 * 3600  # 1 hour

# Data URLs
DATA_ATTEMPTS = 3
DATA_TIMEOUT = 30
DATA_RTD = 15
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)'
URL_BASE = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data'

# Time
TIME_BETWEEN_RESOURCES = 15
TIME_BETWEEN_TWEETS = 10 * 60  # 10 minutes

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

# Twitter
HASHTAG_LIST = '#coronavirus #covid19'

# Icons
ICON_UP = '⬆️'
ICON_DOWN = '⬇️'

# Flags
FLAG_DEFAULT = random.choice(['🌍', '🌎', '🌎'])
FLAGS = {
    'Armenia': '🇦🇲',
    'Russia': '🇷🇺',
    'Monaco': '🇲🇨',
    'South Korea': '🇰🇷',
    'Ecuador': '🇪🇨',
    'Lebanon': '🇱🇧',
    'Spain': '🇪🇸',
    'US': '🇺🇸',
    'Switzerland': '🇨🇭',
    'Saudi Arabia': '🇸🇦',
    'Israel': '🇮🇱',
    'Italy': '🇮🇹',
    'Canada': '🇨🇦',
    'Singapore': '🇸🇬',
    'Afghanistan': '🇦🇫',
    'India': '🇮🇳',
    'Croatia': '🇭🇷',
    'Norway': '🇳🇴',
    'Denmark': '🇩🇰',
    'Senegal': '🇸🇳',
    'Macau': '🇲🇴',
    'Latvia': '🇱🇻',
    'Belarus': '🇧🇾',
    'North Macedonia': '🇲🇰',
    'Sri Lanka': '🇱🇰',
    'UK': '🇬🇧',
    'Romania': '🇷🇴',
    'Estonia': '🇪🇪',
    'Dominican Republic': '🇩🇴',
    'Azerbaijan': '🇦🇿',
    'Indonesia': '🇮🇩',
    'Brazil': '🇧🇷',
    'Ireland': '🇮🇪',
    'Georgia': '🇬🇪',
    'Japan': '🇯🇵',
    'Pakistan': '🇵🇰',
    'Cambodia': '🇰🇭',
    'Iceland': '🇮🇸',
    'France': '🇫🇷',
    'Malaysia': '🇲🇾',
    'Austria': '🇦🇹',
    'Nigeria': '🇳🇬',
    'Germany': '🇩🇪',
    'Bahrain': '🇧🇭',
    'San Marino': '🇸🇲',
    'Qatar': '🇶🇦',
    'Lithuania': '🇱🇹',
    'Mainland China': '🇨🇳',
    'Philippines': '🇵🇭',
    'Oman': '🇴🇲',
    'Algeria': '🇩🇿',
    'United Arab Emirates': '🇦🇪',
    'Vietnam': '🇻🇳',
    'Morocco': '🇲🇦',
    'Iraq': '🇮🇶',
    'Kuwait': '🇰🇼',
    'Belgium': '🇧🇪',
    'Hong Kong': '🇭🇰',
    'Andorra': '🇦🇩',
    'Finland': '🇫🇮',
    'Netherlands': '🇳🇱',
    'Luxembourg': '🇱🇺',
    'Czech Republic': '🇨🇿',
    'Thailand': '🇹🇭',
    'Portugal': '🇵🇹',
    'Iran': '🇮🇷',
    'Egypt': '🇪🇬',
    'Sweden': '🇸🇪',
    'New Zealand': '🇳🇿',
    'Taiwan': '🇹🇼',
    'Australia': '🇦🇺',
    'Greece': '🇬🇷',
    'Mexico': '🇲🇽',
    'Nepal': '🇳🇵'
}
