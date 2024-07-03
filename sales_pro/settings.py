from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@)-b90yh)-4^szo%c_)n(k(4+4#wshsez2!#vcem+44esy!nt#'

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
    'rest_framework',
    'corsheaders',
    'session',
    'tenants',
)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.humanize',
    'rest_framework',
    'session',
    'analytics',
    'branches',
    'branches_others',
    'human_resources',
    'supply_chain',
    'products',
    'corsheaders'
)

SITE_ID = 1
TENANT_APPS_DIR = os.path.join(BASE_DIR, TENANT_APPS[0])
sys.path.insert(0, TENANT_APPS_DIR)
sys.path.insert(0, BASE_DIR)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = "tenants.Tenant"  # app.Model

TENANT_DOMAIN_MODEL = "tenants.Domain"  # app.Model

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

MIDDLEWARE = [
    'django_tenants.middleware.TenantMiddleware',
	'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ORIGINS = 'http://restful.localhost:5173/'

CORS_ALLOW_HEADERS = "*"

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    "http://localhost:5173",
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
