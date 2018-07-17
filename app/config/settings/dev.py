from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True
ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

INSTALLED_APPS += [
    'storages',
    'django_extensions',
]
# DB
DATABASES = secrets['DATABASES']

# Media
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'
