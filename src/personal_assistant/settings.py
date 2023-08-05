
"""
Django settings for personal_assistant project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
import logging
import openai
import os
from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()

environ.Env.read_env(BASE_DIR / ".env")
# print(f'{BASE_DIR} ~~ YOUR BASE_DIR')

# /Users/ekaterina/Documents/GitHub/Personal-Assistant-Django
Secret_Key = env("SECRET_KEY")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Secret_Key
# print(f'{SECRET_KEY} SECRETTTTTTTTTTTTT')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usersapp',
    # 'ai_chat_bot',
    'contactsapp',
    'notesapp',
    'newsapp',
    # 'cloud_storageapp',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personal_assistant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'personal_assistant.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
"""Local PostgreSQL"""
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': env('DATABASE_NAME'),
         'USER': env('DATABASE_USER'),
         'PASSWORD': env('DATABASE_PASSWORD'),
         'HOST': env('DATABASE_HOST'),
         'PORT': env('DATABASE_PORT'),
     }
 }

# # """Cloud Elephant PostgreSQL"""
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env('ELEPHANT_DATABASE_NAME'),
#         'USER': env('ELEPHANT_DATABASE_USER'),
#         'PASSWORD': env('ELEPHANT_DATABASE_PASSWORD'),
#         'HOST': env('ELEPHANT_DATABASE_HOST'),
#         'PORT': env('ELEPHANT_DATABASE_PORT'),
#     }
# }

# print(env('DATABASE_NAME'),  env('DATABASE_USER'), env('DATABASE_PASSWORD'), env('DATABASE_HOST'), env('DATABASE_PORT'))

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


AUTH_USER_MODEL = 'usersapp.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static')
print(STATIC_ROOT)


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# """For Meta UA"""
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_PORT = env('EMAIL_PORT')
# EMAIL_STARTTLS = True
# # EMAIL_USE_SSL = True
# # EMAIL_USE_TLS = True
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL = env('EMAIL_HOST_USER')
# RECIPIENTS_EMAIL = []
#
"""For Gmail"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('GMAIL_HOST')
EMAIL_PORT = env('GMAIL_PORT')
# EMAIL_STARTTLS = False
# EMAIL_USE_SSL = True
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('GMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('GMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('GMAIL_HOST_USER')