from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import datetime

from tools.elastic.manager import ElasticSearchManager
from tools import logger


# @periodic_task(run_every = crontab(hour = '*/1'), name = 'index_anime')
@shared_task()
def index_anime():
    try:
        # TODO нужно вынести этот код отдельно и для каждого таска
        start = datetime.now()

        data_type = 'anime'
        es_manager = ElasticSearchManager()
        es_manager.create_index(data_type)
        es_manager.fill_index(data_type)

        end = datetime.now()
        run_time = end - start
        logger.write('Task "index_anime" отработал успешно за ' + str(run_time.seconds) + ' сек.', logger.TASK)
    except Exception as error:
        logger.write('Task "index_anime" отработала с ошибкой: \n' + str(error), logger.TASK)
