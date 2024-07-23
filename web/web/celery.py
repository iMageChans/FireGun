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
    'get_currency_reserves': {
        'task': 'amm.tasks.get_currency_reserves',
        'schedule': timedelta(seconds=60 * 5),
    },
    'get_burning_totals': {
        'task': 'burning.tasks.get_burning_totals',
        'schedule': timedelta(seconds=60 * 5),
    },
}