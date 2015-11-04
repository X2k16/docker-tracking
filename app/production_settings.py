# encoding=utf-8

from tracking.settings import *

STATIC_ROOT = "/app/static"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/sqlite3/db.sqlite3',
    }
}
