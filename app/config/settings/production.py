from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    'localhost',
]

WSGI_APPLICATION = 'config.wsgi.production.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
