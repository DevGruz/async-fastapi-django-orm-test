import os
from pathlib import Path

import django
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEV')

SECRET_KEY = os.getenv('SECRET_KEY')

INSTALLED_APPS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / os.getenv('DB_FILE', 'sqlite3.db'),
    }
}

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'ru-ru')

TIME_ZONE = os.getenv('TIME_ZONE', 'Europe/Moscow')

USE_I18N = os.getenv('USE_I18N', 'True') == 'True'

USE_TZ = os.getenv('USE_TZ', 'True') == 'True'

SERVER_HOST = os.getenv('SERVER_HOST', '127.0.0.1')

SERVER_PORT = int(os.getenv('SERVER_PORT', 8000))

django.setup()
