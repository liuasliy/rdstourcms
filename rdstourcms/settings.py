# -*- coding: UTF-8 -*-
"""
Django settings for rdstourcms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '))i!n29pdpd3$o6^+zvma#1v+sw+87i3aic7d3(c24_xx=_2y)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'userena',
    'guardian',
    'easy_thumbnails',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_comments',
    'blog',
    'pagination',
    'ckeditor',
    'ckeditor_uploader',
    'favourite',
    'accounts',
    
)
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.MyProfile'  
  
USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

SITE_ID = 1


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)



TEMPLATE_CONTEXT_PROCESSORS = (
    #"django.core.context_processors.auth",
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request"
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
)



ROOT_URLCONF = 'rdstourcms.urls'

WSGI_APPLICATION = 'rdstourcms.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rdstourcms',
        'USER': 'root',                       # Not used with sqlite3.
        'PASSWORD': '12344',                   # Not used with sqlite3.
        'HOST': 'localhost',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
SITE_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = "./media/"
CKEDITOR_UPLOAD_PATH = './media/upload/'


DIR_Admin = './static/admin/'
CSS_DIR = './static/css/'
JS_DIR = './static/js/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("images", os.path.join(STATIC_ROOT, 'images')),
    ("bootstrap", os.path.join(STATIC_ROOT, 'bootstrap')),
    ("style", os.path.join(STATIC_ROOT, 'style')),
    ("components", os.path.join(STATIC_ROOT, 'components')),
    ("exampic", os.path.join(STATIC_ROOT, 'exampic')),
    ("img", os.path.join(STATIC_ROOT, 'img')),
    ("slider", os.path.join(STATIC_ROOT, 'slider')),
    ("fonts", os.path.join(STATIC_ROOT, 'fonts')),
)
# old settings // TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

WEB_ROOT = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
TEMPLATE_DIRS = (
    os.path.join(WEB_ROOT, '../templates').replace('\\', '/'),
    )


# 后台模板配置
SUIT_CONFIG = {
    'ADMIN_NAME': u'路人行',
    'MENU': (
        'sites',
        {'app': 'auth', 'label': u'认证管理'},
        {'app': 'blog', 'label': u'博客'},
        {'app': 'accounts', 'label': u'用户管理'},
        {'app': 'django_comments', 'label': u'评论'},
        {'app': 'favourite', 'label': u'收藏夹'},

    ),
}

# ckeditor编辑器配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format','Bold', 'Italic', 'Underline'],
            ['Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
            ['TextColor', 'BGColor'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField'],
            ['Maximize']
        ],
        'height': 300,
        'width': '100%',
    },
}