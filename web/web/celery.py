# web/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

app = Celery('web')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'get_currency_reserves_celery': {
        'task': 'amm.tasks.get_currency_reserves_celery',
        'schedule': timedelta(seconds=60),
    },
    'get_burning_totals_celery': {
        'task': 'burning.tasks.get_burning_totals_celery',
        'schedule': timedelta(seconds=60),
    },
    'get_accumulative_reward_pool_celery': {
        'task': 'mining.tasks.get_accumulative_reward_pool_celery',
        'schedule': timedelta(seconds=60),
    },
    'get_merchant_volume_celery': {
        'task': 'mining.tasks.get_merchant_volume_celery',
        'schedule': timedelta(seconds=60),
    },
    'get_total_volume_celery': {
        'task': 'mining.tasks.get_total_volume_celery',
        'schedule': timedelta(seconds=60),
    },
    'get_vote_limit_celery': {
        'task': 'node.tasks.get_vote_limit_celery',
        'schedule': timedelta(seconds=60),
    },
    'get_node_ranks': {
        'task': 'voting.tasks.get_node_ranks',
        'schedule': timedelta(seconds=180),
    },
}