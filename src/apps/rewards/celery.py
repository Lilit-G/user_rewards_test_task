import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')

app = Celery('rewards', broker=redis_url, backend=redis_url)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
