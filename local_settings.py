import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mula',
        'USER': 'bram',
        'PASSWORD': 'bram',
        'HOST': 'localhost',
        'PORT': '',
    }
}
