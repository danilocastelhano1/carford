from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        """
        Creates automatically an user to test the API
        """
        from django.contrib.auth.models import User

        if not User.objects.filter(username="admin").exists():
            User.objects.create_user(username="admin", password="123456")
