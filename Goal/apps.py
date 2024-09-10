from django.apps import AppConfig


class GoalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Goal'
def ready(self):
        import Goal.signals