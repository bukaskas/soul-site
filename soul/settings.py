"""
Django settings for soul project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import environ


# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get('DEBUG')) == '1'

ALLOWED_HOSTS = [
    'soul-kitesurfing.up.railway.app',
    'localhost',
     'http://127.0.0.1:8000',
     "127.0.0.1"
]

# if not DEBUG:
#     ALLOWED_HOSTS += [os.environ.get('ALLOWED_HOST')]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'storages',
    'rest_framework',
    'website',
    "corsheaders",
    "django_filters",
    "django_extensions",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",

]

CORS_ALLOWED_ORIGINS = [
   'https://soul-kitesurfing.up.railway.app',
   'http://127.0.0.1:8000'
]

CSRF_TRUSTED_ORIGINS=[
   'https://soul-kitesurfing.up.railway.app',
   'https://*.railway.app/'
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ROOT_URLCONF = 'soul.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'soul.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': os.environ.get("PGDATABASE"),
        'USER': os.environ.get("PGUSER"),
        'PASSWORD': os.environ.get("PGPASSWORD"),
        'HOST': os.environ.get("PGHOST"),
        'PORT': os.environ.get("PGPORT"),
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_ROOT = BASE_DIR/'staticfiles'



STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR,'static/images')


STATIC_URL = 'static/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATICFILES_DIRS=[
#     BASE_DIR/'static'
# ]



USE_L10N = False

DATE_INPUT_FORMATS = ('%d/%m/%Y','%d-%m-%Y','%Y-%m-%d')


# Static file SETUP

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_STORAGE_REGION_NAME = 'EU (Frankfurt) eu-central-1'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'