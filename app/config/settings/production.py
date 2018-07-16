import sys
from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

# Django가 runserver로 켜졌는지 확인
RUNSERVER = sys.argv[1] == 'runserver'
DEBUG = False
ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

# runserver로 production환경을 실행할 경우
if RUNSERVER:
    DEBUG = True
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
    ]

WSGI_APPLICATION = 'config.wsgi.production.application'
INSTALLED_APPS += [
    'storages',
]

# DB
DATABASES = secrets['DATABASES']

# Media
DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

# Log
# /var/log/django 디렉토리가 존재하면 LOG_DIR로 그대로 사용
# 없으면 ROOT_DIR/.log디렉토리를 사용 (없으면 생성)
LOG_DIR = '/var/log/django'
if not os.path.exists(LOG_DIR):
    LOG_DIR = os.path.join(ROOT_DIR, '.log')
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'django.server',
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 10485760,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_error'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
