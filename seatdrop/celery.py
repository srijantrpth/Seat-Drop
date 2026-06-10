import os 
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seatdrop.settings')
app = Celery('seatdrop')
app.config_from_object('seatdrop.settings', namespace='CELERY')
app.autodiscover_tasks()