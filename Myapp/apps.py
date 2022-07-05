from django.apps import AppConfig

# this is the django app, App is one part of small project, where we have performed some or more project functionlity
# We can create number of App in one project

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Myapp'
