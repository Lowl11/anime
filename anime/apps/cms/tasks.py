from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab

from tools.elastic.manager import ElasticSearchManager


# @periodic_task(run_every = crontab(minute = '*/1'), name = 'test_task')
@shared_task()
def index_anime():
    data_type = 'anime'
    es_manager = ElasticSearchManager()
    es_manager.create_index(data_type)
    es_manager.fill_index(data_type)
