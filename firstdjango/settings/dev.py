from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DJANGO_MARIADB',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3309'
    },
    'mariadb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DJANGO_MARIADB',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3309'
    }
}