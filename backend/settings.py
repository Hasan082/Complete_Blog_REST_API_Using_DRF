"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8g9dt2zcqymxd8z6=om!dqod()2*3_8je=#livnngv-bpgpm%m"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = [
    "jazzmin",  # Django admin interface customization
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "api",
    "blog",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "django_cleanup.apps.CleanupConfig",
    "drf_spectacular",
    "corsheaders", 
]

# Add all apps to INSTALLED_APPS
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "backend" / "static"]
# STATIC_ROOT = BASE_DIR / "staticfiles"  # For production use, uncomment this line to collect static files


# Media files (User-uploaded content)
# https://docs.djangoproject.com/en/5.0/topics/files/   
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

REST_FRAMEWORK = {
    # Use DRF Permissions
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    # Spectacular settings
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
   
}

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",  # Adjust this to your frontend URL
]
CORS_ALLOW_ALL_ORIGINS = True

# GLOBAL PAGINATION CLASS
# Uncomment and set pagination class in "REST_FRAMEWORK" if you have one
# "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
# "PAGE_SIZE": 10,  # Adjust the number as needed

# "DEFAULT_PAGINATION_CLASS": "blog.pagination.BlogPagination",
# "PAGE_SIZE": 10

SPECTACULAR_SETTINGS = {
    "TITLE": "Complete Blog REST API",
    "DESCRIPTION": "Complete Blog REST API with all possible functionality",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}


# Jazzmin settings
# For more information, see https://django-jazzmin.readthedocs.io/en/latest

JAZZMIN_SETTINGS = {
    "site_title": "Blog Admin",
    "site_header": "MY Blog",
    "site_brand": "My Blog",
    "site_logo": "dash_img/logo.png",
    "login_logo": "dash_img/logo.png",
    "site_logo_classes": "img-fluid",
    "site_icon": "backend/img/favicon.png",
    "welcome_sign": "Welcome to Our Blog",
    "copyright": "@MD HASANUZZAMAN",
    "search_model": ["auth.User", "auth.Group"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "blog"},
    ],
    "usermenu_links": "",  # [{"model": "auth.user"}],
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["auth", "blog", "blog.author", "blog.blog"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
        "blog": "fas fa-blog",
        "blog.blog": "fas fa-newspaper",  # Blog posts
        "blog.author": "fas fa-user-edit",  # Author profile
        "blog.category": "fas fa-folder-open",  # Blog categories (if you have one)
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": "css/custom.css",
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": True,
}


# Django Cleanup settings
# Automatically delete old files when a new file is uploaded
CLEANUP_ENABLED = True
CLEANUP_IGNORE_UNMATCHED = True  # Prevent deletion if no file is found (safety)
CLEANUP_VERBOSE = True  # Show logs during file deletion (helpful for debug)
