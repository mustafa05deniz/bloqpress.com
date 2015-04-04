
import os.path
burasi = os.path.dirname(__file__)
ustDizin=os.path.split(burasi)[0]

TEMPLATE_DIRS=(
    os.path.join(ustDizin,'yonetim/sablonlar'),

)
STATICFILES_DIRS = (

    os.path.join(ustDizin,'statik_dosyalar'),
     '/home/django/statik_dosyalar/',

)

MEDIA_ROOT = ("/home/django/django_project/statik_dosyalar/media")

SECRET_KEY = 'ppPho5jhtd6bqHtLTa90XUq5Ts7HwycHDCtlrvJrwkMkv084uF'



DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yonetim',
    'redactor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ustDizin, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
