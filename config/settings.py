"""
Django settings for Quran API project.
Yaxshilangan: Django 6.x, Jazzmin admin, caching, import/export, drf-spectacular
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-only-for-dev')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv(
    'CSRF_TRUSTED_ORIGINS',
    'https://quranapi-mabx.onrender.com,http://localhost:8000'
).split(',')


# ─────────────────────────────────────────────
# Jazzmin — Chiroyli Admin Panel Sozlamalari
# ─────────────────────────────────────────────
JAZZMIN_SETTINGS = {
    "site_title": "Quran API Admin",
    "site_header": "🕌 Quran API",
    "site_brand": "Quran API",
    "welcome_sign": "Assalomu alaykum! Quran API admin paneliga xush kelibsiz.",
    "copyright": "Quran API — asadbekoffical1202@gmail.com",
    "search_model": ["quran.Sura", "quran.Ayah", "quran.Author"],
    "user_avatar": None,

    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Swagger API", "url": "/api/v3/schema/swagger-ui/", "new_window": True},
        {"name": "Sayt", "url": "/", "new_window": True},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "quran.Sura": "fas fa-book-quran",
        "quran.Ayah": "fas fa-align-left",
        "quran.Author": "fas fa-user-tie",
        "quran.QuranBook": "fas fa-file-pdf",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,

    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },

    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-teal",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}


# ─────────────────────────────────────────────
# O'rnatilgan ilovalar
# ─────────────────────────────────────────────
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework',
    'rest_framework.authtoken',
    'import_export',
    'django_filters',
    'drf_spectacular',

    # Mahalliy ilovalar
    'quran',          # Unified app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# ─────────────────────────────────────────────
# Ma'lumotlar bazasi — MySQL (TiDB Cloud)
# ─────────────────────────────────────────────
import pymysql
pymysql.install_as_MySQLdb()   # PyMySQL → MySQLdb sifatida ishlaydi

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.getenv('DB_DATABASE', 'sys'),
        'USER': os.getenv('DB_USERNAME', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'ssl': {'ca': None},   # TiDB Cloud SSL (sertifikatsiz rejim)
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'connect_timeout': 10,
        },
    }
}


# ─────────────────────────────────────────────
# Cache (tezkorlik uchun)
# ─────────────────────────────────────────────
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'quran-api-cache',
        'TIMEOUT': 900,  # 15 daqiqa
        'OPTIONS': {
            'MAX_ENTRIES': 5000,
        }
    }
}


# ─────────────────────────────────────────────
# Django REST Framework
# ─────────────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 30,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}


# ─────────────────────────────────────────────
# drf-spectacular — Swagger/OpenAPI
# ─────────────────────────────────────────────
SPECTACULAR_SETTINGS = {
    'TITLE': "📖 Qur'on API",
    'DESCRIPTION': (
        "Bu API orqali siz Qur'oni Karimning oyatlari, suralari va "
        "ma'nolarini o'zbek, arab, rus va ingliz tillarida topishingiz mumkin. "
        "Audiolari bilan birga.\n\n"
        "**Muallif:** asadbekoffical1202@gmail.com\n"
        "**Telegram:** @asadbek_074"
    ),
    'VERSION': 'v3.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'TAGS': [
        {'name': 'Suralar', 'description': "Qur'on suralari"},
        {'name': 'Oyatlar', 'description': "Qur'on oyatlari"},
        {'name': 'Mualliflar', 'description': 'Tarjimonlar va qorilar'},
        {'name': 'Kitoblar', 'description': "Qur'on PDF kitoblari"},
    ],
}


# ─────────────────────────────────────────────
# Import-Export (Excel)
# ─────────────────────────────────────────────
IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_SKIP_ADMIN_LOG = False


# ─────────────────────────────────────────────
# Parol tekshirish
# ─────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ─────────────────────────────────────────────
# Til va vaqt mintaqasi
# ─────────────────────────────────────────────
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True


# ─────────────────────────────────────────────
# Statik va media fayllar
# ─────────────────────────────────────────────
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = []  # Agar maxsus static papkangiz bo'lsa qo'shing

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
