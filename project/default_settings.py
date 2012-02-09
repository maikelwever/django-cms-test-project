import os
gettext = lambda s: s
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = PROJECT_DIR

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATIC_ROOT = 'static_root/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

ADMINS = (
# ('Your Name', 'your_email@example.com'),
    ('Maikel Wever', 'maikelwever@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Amsterdam'

LANGUAGE_CODE = 'nl'

SITE_ID = 1

USE_I18N = True

USE_L10N = True


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
# default template context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'zinnia.context_processors.version',
)

ROOT_URLCONF = 'urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.staticfiles',
# Project

# django-cms
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'cms.plugins.text',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.video',
    'cms.plugins.file',
    'zinnia',
    'tagging',
    'zinnia.plugins',
    'django.contrib.comments',
# 3rd party
    'django_extensions',
    #'django.contrib.admindocs',
)



LOGIN_URL = "/user/login/"
LOGIN_REDIRECT_URL = "/"

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)
LANGUAGES = [
    ('en', 'English'),
]

ZINNIA_ENTRY_BASE_MODEL = 'zinnia.plugins.placeholder.EntryPlaceholder'
