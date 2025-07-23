from django.apps import AppConfig


class PrestatairesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.prestataires'

    def ready(self):
        import apps.prestataires.signals    

class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.services' 