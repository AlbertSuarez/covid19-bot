from apscheduler.schedulers.blocking import BlockingScheduler

from src.config import MAX_INSTANCES, GRACE_TIME
from src.cron import runner
from src.helper import log


scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', hour='*', minute='0,10,20,30,40,50',
                         max_instances=MAX_INSTANCES, misfire_grace_time=GRACE_TIME)
def run():
    """
    Main function for running the bot.
    :return: Iteration done.
    """
    log.info('Job started!')
    runner.run()
    log.info('Job ended!')
