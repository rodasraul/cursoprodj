from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rhodas_db',
        'USER': 'rhodas',
        'PASSWORD': 'c7e9n0n4u1x',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
#STATICFILES_DIRS = BASE_DIR.child('static')
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
# Carpeta principal para archivos multimedia
# MEDIA_ROOT = [BASE_DIR / 'media']
# MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
