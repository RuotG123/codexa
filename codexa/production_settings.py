# codexa/production_settings.py
from .settings import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Add your PythonAnywhere domain
ALLOWED_HOSTS = ['ruotg123.pythonanywhere.com', 'localhost', '127.0.0.1']

# Static files configuration for production
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ruotg123/codexa/static'

# Media files (if you add file uploads later)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ruotg123/codexa/media'

# Database for production (using SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/ruotg123/codexa/db.sqlite3',
    }
}

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Generate a new secret key for production
SECRET_KEY = 'django-production-key-change-this-to-something-very-random-and-secure'

# Additional security settings (optional but recommended)
SECURE_SSL_REDIRECT = False  # Set to True if you have SSL
SESSION_COOKIE_SECURE = False  # Set to True if you have SSL
CSRF_COOKIE_SECURE = False  # Set to True if you have SSL

# Logging configuration (optional)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/home/ruotg123/codexa/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}