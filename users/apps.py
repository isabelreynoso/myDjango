from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    path = '/Users/Student/Desktop/django_project/users'

    def ready(self):
        import users.signals
