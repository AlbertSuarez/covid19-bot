# CoVid-19 bot

[![HitCount](http://hits.dwyl.io/AlbertSuarez/covid19-bot.svg)](http://hits.dwyl.io/AlbertSuarez/covid19-bot)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/covid19-bot.svg)](https://GitHub.com/AlbertSuarez/covid19-bot/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/covid19-bot.svg)](https://GitHub.com/AlbertSuarez/covid19-bot/network/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/AlbertSuarez/covid19-bot.svg)](https://github.com/AlbertSuarez/covid19-bot)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/covid19-bot.svg)](https://GitHub.com/AlbertSuarez/covid19-bot/graphs/contributors/)
[![GitHub license](https://img.shields.io/github/license/AlbertSuarez/covid19-bot.svg)](https://github.com/AlbertSuarez/covid19-bot/blob/master/LICENSE)

[Twitter account](https://twitter.com/coronavid19_bot) | [Static repo website](https://asuarez.dev/covid19-bot/)

🤖 Real time Twitter bot notifying new confirmed Corona virus (CoVid-19) cases, deaths and recovered people by location.

## Data source

Real time data is being retrieved from the [Novel Coronavirus (COVID-19) Cases repository](https://github.com/CSSEGISandData/COVID-19), by [JHU CSSE](https://systems.jhu.edu/research/public-health/ncov/).

## Python requirements

This project is using Python3.7. All these requirements have been specified in the `requirements.lock` file.

1. [Requests](https://2.python-requests.org/en/master/): used for retrieving the HTML content of a website.
2. [Dictdiffer](https://dictdiffer.readthedocs.io/en/latest/): used for checking data differences easier.
3. [APScheduler](https://apscheduler.readthedocs.io/en/stable/): used for scheduling jobs in a certain time.
4. [Twitter](https://python-twitter.readthedocs.io/en/latest/): used for posting tweets.

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run this script, please execute the following from the root directory:

1. Setup virtual environment

2. Install dependencies

  ```bash
  pip3 install -r requirements.lock
  ```

3. Set up [Twitter API](https://developer.twitter.com/) account creating the .env file. This file must have this structure (without the brackets):

  ```
  TWITTER_CONSUMER_KEY={TWITTER_CONSUMER_KEY}
  TWITTER_CONSUMER_SECRET={TWITTER_CONSUMER_SECRET}
  TWITTER_ACCESS_TOKEN_KEY={TWITTER_ACCESS_TOKEN_KEY}
  TWITTER_ACCESS_TOKEN_SECRET={TWITTER_ACCESS_TOKEN_SECRET}
  ```

4. Run the script as a Python module

  ```bash
  python3 -m src
  ```

  or as a Docker container

  ```bash
  docker-compose up -d --build
  ```

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © CoVid-19 bot
