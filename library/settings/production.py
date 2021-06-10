from library.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'namedatabase(DDBB)',
#        'USER': 'nameuser',
#        'PASSWORD': 'password',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
# }   
# Para trabajar con la database tienes que instalar la dependecia o libreria psycopg2.

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'namedatabase(DDBB)',
#        'USER': 'nameuser',
#        'PASSWORD': 'password',
#        'HOST': 'localhost',
#        'PORT': '3306',
#     }
# }
# Para trabajar con la database tienes que instalar la dependecia o libreria mysqlclient.