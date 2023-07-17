import logging

from celery import Celery
from celery.schedules import crontab

from core.settings import settings

logger = logging.getLogger('uvicorn')

scheduler = Celery('scheduler')
scheduler.conf.broker_url = settings.CELERY_BROKER_URL
scheduler.conf.result_backend = settings.CELERY_RESULT_BACKEND
scheduler.autodiscover_tasks()


scheduler.conf.beat_schedule = {
    'every': {
        'task': 'scheduler.remove_outdated_session',
        'schedule': settings.SECURITY.REFRESH_TOKEN_EXPIRE,
    }
}
