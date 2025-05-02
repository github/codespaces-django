import os

settings_module = os.getenv('DJANGO_SETTINGS_MODULE')

if settings_module == 'hello_world.settings.production':
    from .production import *
elif settings_module == 'hello_world.settings.development':
    from .development import *