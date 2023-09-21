import os
from dotenv import load_dotenv
from mysite.settings.base import *

load_dotenv(Path(BASE_DIR).parent / '.env')
print(Path(BASE_DIR).parent)

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = bool(os.environ.get("DEBUG", 1))
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
