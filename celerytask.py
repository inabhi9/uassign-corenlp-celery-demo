from celery import Celery
celery = Celery('client', include=['client'])
celery.config_from_object('config')
