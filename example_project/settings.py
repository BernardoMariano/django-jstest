# coding: utf-8

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'mymedia')
MEDIA_URL = '/mymedia/'
ADMIN_MEDIA_PREFIX = '/myadminmedia/'

ROOT_URLCONF = 'jstest_project.urls'

INSTALLED_APPS = (
    'jstest',
    'myapp',
)