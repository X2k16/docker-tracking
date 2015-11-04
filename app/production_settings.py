# encoding=utf-8

from tracking.settings import *

STATIC_ROOT = "/app/static"
STATIC_URL = "/tracking/static/"

def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/sqlite3/db.sqlite3',
    }
}
