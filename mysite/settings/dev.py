from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "foo"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# python manage.py runserver --settings=mysite.settings.dev