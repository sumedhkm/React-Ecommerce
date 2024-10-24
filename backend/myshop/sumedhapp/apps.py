# sumedhapp/apps.py

from django.apps import AppConfig

class SumedhappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sumedhapp'

    # def ready(self):
    #     import sumedhapp.signals
