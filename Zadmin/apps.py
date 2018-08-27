from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules
from Zadmin.service.zadmin import site

class ZadminConfig(AppConfig):
    name = 'Zadmin'
    def ready(self):
        autodiscover_modules('zadmin', register_to=site)
