from django.apps import AppConfig


class CrochetappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crochetApp'
    def ready(self):
        import crochetApp.signals
