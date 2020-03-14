import time

from src import scheduler
from src.config import DEBUG
from src.helper import log


if __name__ == '__main__':
    try:
        log.info('Covid19-bot was born!')
        if not DEBUG:
            scheduler.scheduler.start()
        else:
            log.info('Running jobs manually since DEBUG is enabled.')
            while True:
                time.sleep(5)
                scheduler.run()
                time.sleep(30)

    except Exception as e:
        log.error(f'Unexpected error {e} in Covid-19')
        log.exception(e)

    finally:
        log.info('Rest in peace, Covid-19.')
