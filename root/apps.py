from django.apps import AppConfig
from django.db.models.signals import pre_save
from Module import MonkeyPatch


class RootConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'root'

    def ready(self):
        MonkeyPatch.monkey_patch_openpyxl()
