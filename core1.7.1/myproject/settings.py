
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '^f-_wny8)q2%_56!bda9-2rs%&(sg0pt64mb%ina$fwr(o)avq'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_conf',

)
BASE_PATH = os.path.join(BASE_DIR, os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, os.path.dirname(__file__)+'/templates')

TEMPLATE_DIRS = (
os.path.join(TEMPLATE_PATH, ''),
)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
os.path.join(BASE_PATH, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_PATH, 'media')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS =(
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    'django.contrib.messages.context_processors.messages',
)


ROOT_URLCONF = 'myproject.urls'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'porselen_test',
        'USER': 'raistmon',                    
        'PASSWORD': '',
        'HOST': '127.0.0.1',                     
        'PORT': '',  

    }
}


LANGUAGE_CODE = 'tr-tr'

TIME_ZONE = "Europe/Istanbul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

