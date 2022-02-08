from django.apps import AppConfig


class TuiterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tuiter'

    def ready(self):
        import tuiter.signals
