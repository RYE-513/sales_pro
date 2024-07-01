from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@)-b90yh)-4^szo%c_)n(k(4+4#wshsez2!#vcem+44esy!nt#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SHARED_APPS = (
    'django_tenants',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'session',
    'tenants',
    'analytics',
    'branches',
    'human_resources',
    'supply_chain',
)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.humanize',
    'session',
    'tenants',
    'analytics',
    'branches',
    'human_resources',
    'supply_chain',

)

SITE_ID = 1
TENANT_APPS_DIR = os.path.join(BASE_DIR, TENANT_APPS[0])
sys.path.insert(0, TENANT_APPS_DIR)
sys.path.insert(0, BASE_DIR)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = "tenants.Tenant"  # app.Model

TENANT_DOMAIN_MODEL = "tenants.Domain"  # app.Model


MIDDLEWARE = [
    'django_tenants.middleware.TenantMiddleware',
	'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'sales_pro.urls'

PUBLIC_SCHEMA_URLCONF = 'sales_pro.urls_public'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'sales_pro.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': os.environ.get('DATABASE_DB', 'sales_pro'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', 5432),
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
MEDIA_URL = '/media/'


MAX_UPLOAD_SIZE = 15 * 1024 * 1024

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
