# DO NOT EDIT THIS FILE!
#
# All configuration must be done in the `configuration.py` file.
# This file is part of the Peering Manager code and it will be overwritten with
# every code releases.


import platform
from pathlib import Path

from django.contrib.messages import constants as messages
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.validators import URLValidator

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
HOSTNAME = platform.node()
BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"

VERSION = "v1.4.1-dev"

if platform.python_version_tuple() < ("3", "6"):
    raise RuntimeError(
        f"Peering Manager requires Python 3.6 or higher (current: Python {platform.python_version()})"
    )

try:
    from peering_manager import configuration
except ImportError:
    raise ImproperlyConfigured(
        "Configuration file is not present. "
        "Please define peering_manager/configuration.py per the documentation."
    )

for setting in ["ALLOWED_HOSTS", "DATABASE", "SECRET_KEY"]:
    if not hasattr(configuration, setting):
        raise ImproperlyConfigured(
            f"Mandatory setting {setting} is not in the configuration.py file."
        )

# Set required parameters
ALLOWED_HOSTS = getattr(configuration, "ALLOWED_HOSTS")
DATABASE = getattr(configuration, "DATABASE")
SECRET_KEY = getattr(configuration, "SECRET_KEY")

# Deprecated, to be removed in 2.0.0
MY_ASN = getattr(configuration, "MY_ASN", None)

CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

BASE_PATH = getattr(configuration, "BASE_PATH", "")
if BASE_PATH:
    BASE_PATH = BASE_PATH.strip("/") + "/"  # Enforce trailing slash only
DEBUG = getattr(configuration, "DEBUG", False)
LOGGING = getattr(configuration, "LOGGING", {})
REDIS = getattr(configuration, "REDIS", {})
CACHE_TIMEOUT = getattr(configuration, "CACHE_TIMEOUT", 0)
CHANGELOG_RETENTION = getattr(configuration, "CHANGELOG_RETENTION", 90)
LOGIN_REQUIRED = getattr(configuration, "LOGIN_REQUIRED", False)
BANNER_LOGIN = getattr(configuration, "BANNER_LOGIN", "")
NAPALM_USERNAME = getattr(configuration, "NAPALM_USERNAME", "")
NAPALM_PASSWORD = getattr(configuration, "NAPALM_PASSWORD", "")
NAPALM_TIMEOUT = getattr(configuration, "NAPALM_TIMEOUT", 30)
NAPALM_ARGS = getattr(configuration, "NAPALM_ARGS", {})
PAGINATE_COUNT = getattr(configuration, "PAGINATE_COUNT", 20)
METRICS_ENABLED = getattr(configuration, "METRICS_ENABLED", False)

DATE_FORMAT = getattr(configuration, "DATE_FORMAT", "jS F, Y")
DATETIME_FORMAT = getattr(configuration, "DATETIME_FORMAT", "jS F, Y G:i")
SHORT_DATE_FORMAT = getattr(configuration, "SHORT_DATE_FORMAT", "Y-m-d")
SHORT_DATETIME_FORMAT = getattr(configuration, "SHORT_DATETIME_FORMAT", "Y-m-d H:i")
SHORT_TIME_FORMAT = getattr(configuration, "SHORT_TIME_FORMAT", "H:i:s")
TIME_FORMAT = getattr(configuration, "TIME_FORMAT", "G:i")
try:
    with open("/etc/timezone", "r") as f:
        BASE_TZ = f.readline()

    # For some reasons, Django does not seem to be happy about this particular value
    if "Etc/UTC" in BASE_TZ:
        raise Exception("Unsupported TZ")
except (IOError, Exception):
    BASE_TZ = "UTC"

TIME_ZONE = getattr(configuration, "TIME_ZONE", BASE_TZ).rstrip()
EMAIL = getattr(configuration, "EMAIL", {})
BGPQ3_PATH = getattr(configuration, "BGPQ3_PATH", "bgpq3")
BGPQ3_HOST = getattr(configuration, "BGPQ3_HOST", "whois.radb.net")
BGPQ3_SOURCES = getattr(
    configuration,
    "BGPQ3_SOURCES",
    "RIPE,APNIC,AFRINIC,ARIN,NTTCOM,ALTDB,BBOI,BELL,JPIRR,LEVEL3,RADB,RGNET,TC",
)
BGPQ3_ARGS = getattr(
    configuration,
    "BGPQ3_ARGS",
    {"ipv6": ["-r", "16", "-R", "48"], "ipv4": ["-r", "8", "-R", "24"]},
)

# Pagination
PER_PAGE_SELECTION = [25, 50, 100, 250, 500, 1000]
if PAGINATE_COUNT not in PER_PAGE_SELECTION:
    PER_PAGE_SELECTION.append(PAGINATE_COUNT)
    PER_PAGE_SELECTION = sorted(PER_PAGE_SELECTION)


# Django filters
FILTERS_NULL_CHOICE_LABEL = "-- None --"
FILTERS_NULL_CHOICE_VALUE = "null"


# Use major.minor as API version
REST_FRAMEWORK_VERSION = VERSION[0:3]
REST_FRAMEWORK = {
    "DEFAULT_VERSION": REST_FRAMEWORK_VERSION,
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.AcceptHeaderVersioning",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "peering_manager.api.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["peering_manager.api.TokenPermissions"],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": PAGINATE_COUNT,
}


# Case insensitive search for tags
TAGGIT_CASE_INSENSITIVE = True


# NetBox API configuration
NETBOX_API = getattr(configuration, "NETBOX_API", "")
NETBOX_API_TOKEN = getattr(configuration, "NETBOX_API_TOKEN", "")
NETBOX_API_THREADING = getattr(configuration, "NETBOX_API_THREADING", False)
NETBOX_API_VERIFY_SSL = getattr(configuration, "NETBOX_API_VERIFY_SSL", True)
NETBOX_DEVICE_ROLES = getattr(
    configuration, "NETBOX_DEVICE_ROLES", ["router", "firewall"]
)

# PeeringDB URLs
PEERINGDB_API = "https://peeringdb.com/api/"
PEERINGDB = "https://peeringdb.com/asn/"
# To be removed in v2.0
PEERINGDB_USERNAME = getattr(configuration, "PEERINGDB_USERNAME", "")
PEERINGDB_PASSWORD = getattr(configuration, "PEERINGDB_PASSWORD", "")
PEERINGDB_API_KEY = getattr(configuration, "PEERINGDB_API_KEY", "")

# GitHub releases check
RELEASE_CHECK_URL = getattr(
    configuration,
    "RELEASE_CHECK_URL",
    "https://api.github.com/repos/peering-manager/peering-manager/releases",
)
RELEASE_CHECK_TIMEOUT = getattr(configuration, "RELEASE_CHECK_TIMEOUT", 86400)

# Validate repository URL and timeout
if RELEASE_CHECK_URL:
    try:
        URLValidator(RELEASE_CHECK_URL)
    except ValidationError:
        raise ImproperlyConfigured(
            "RELEASE_CHECK_URL must be a valid API URL. "
            "Example: https://api.github.com/repos/peering-manager/peering-manager"
        )
if RELEASE_CHECK_TIMEOUT < 3600:
    raise ImproperlyConfigured(
        "RELEASE_CHECK_TIMEOUT must be at least 3600 seconds (1 hour)"
    )


try:
    from peering_manager.ldap_config import *

    LDAP_CONFIGURED = True
except ImportError:
    LDAP_CONFIGURED = False

# If LDAP is configured, load the config
if LDAP_CONFIGURED:
    try:
        import django_auth_ldap
        import ldap

        # Prepend LDAPBackend to the default ModelBackend
        AUTHENTICATION_BACKENDS = [
            "django_auth_ldap.backend.LDAPBackend",
            "django.contrib.auth.backends.ModelBackend",
        ]
    except ImportError:
        raise ImproperlyConfigured(
            "LDAP authentication has been configured, but django-auth-ldap is not "
            "installed. You can remove peering_manager/ldap_config.py to disable "
            "LDAP."
        )

try:
    from peering_manager.radius_config import *

    RADIUS_CONFIGURED = True
except ImportError:
    RADIUS_CONFIGURED = False

if RADIUS_CONFIGURED:
    try:
        import radiusauth

        # Prepend RADIUSBackend to the default ModelBackend
        AUTHENTICATION_BACKENDS = [
            "radiusauth.backends.RADIUSBackend",
            "django.contrib.auth.backends.ModelBackend",
        ]
    except ImportError:
        raise ImproperlyConfigured(
            "RADIUS authentication has been configured, but django-radius is not "
            "installed. You can remove peering_manager/radius_config.py to disable "
            "RADIUS."
        )

# Force PostgreSQL to be used as database backend
configuration.DATABASE.update({"ENGINE": "django.db.backends.postgresql"})
# Actually set the database's settings
DATABASES = {"default": configuration.DATABASE}


# Redis
# Background task queuing
if "tasks" not in REDIS:
    raise ImproperlyConfigured(
        "REDIS section in configuration.py is missing the 'tasks' subsection."
    )
TASKS_REDIS = REDIS["tasks"]
TASKS_REDIS_HOST = TASKS_REDIS.get("HOST", "localhost")
TASKS_REDIS_PORT = TASKS_REDIS.get("PORT", 6379)
TASKS_REDIS_SENTINELS = TASKS_REDIS.get("SENTINELS", [])
TASKS_REDIS_USING_SENTINEL = all(
    [isinstance(TASKS_REDIS_SENTINELS, (list, tuple)), len(TASKS_REDIS_SENTINELS) > 0]
)
TASKS_REDIS_SENTINEL_SERVICE = TASKS_REDIS.get("SENTINEL_SERVICE", "default")
TASKS_REDIS_PASSWORD = TASKS_REDIS.get("PASSWORD", "")
TASKS_REDIS_DATABASE = TASKS_REDIS.get("DATABASE", 0)
TASKS_REDIS_DEFAULT_TIMEOUT = TASKS_REDIS.get("DEFAULT_TIMEOUT", 300)
TASKS_REDIS_SSL = TASKS_REDIS.get("SSL", False)
# Caching
if "caching" not in REDIS:
    raise ImproperlyConfigured(
        "REDIS section in configuration.py is missing caching subsection."
    )
CACHING_REDIS = REDIS["caching"]
CACHING_REDIS_HOST = CACHING_REDIS.get("HOST", "localhost")
CACHING_REDIS_PORT = CACHING_REDIS.get("PORT", 6379)
CACHING_REDIS_SENTINELS = CACHING_REDIS.get("SENTINELS", [])
CACHING_REDIS_USING_SENTINEL = all(
    [
        isinstance(CACHING_REDIS_SENTINELS, (list, tuple)),
        len(CACHING_REDIS_SENTINELS) > 0,
    ]
)
CACHING_REDIS_SENTINEL_SERVICE = CACHING_REDIS.get("SENTINEL_SERVICE", "default")
CACHING_REDIS_PASSWORD = CACHING_REDIS.get("PASSWORD", "")
CACHING_REDIS_DATABASE = CACHING_REDIS.get("DATABASE", 0)
CACHING_REDIS_DEFAULT_TIMEOUT = CACHING_REDIS.get("DEFAULT_TIMEOUT", 300)
CACHING_REDIS_SSL = CACHING_REDIS.get("SSL", False)

if CACHING_REDIS_USING_SENTINEL:
    CACHEOPS_SENTINEL = {
        "locations": CACHING_REDIS_SENTINELS,
        "service_name": CACHING_REDIS_SENTINEL_SERVICE,
        "db": CACHING_REDIS_DATABASE,
    }
else:
    REDIS_CACHE_CON_STRING = "rediss://" if CACHING_REDIS_SSL else "redis://"
    if CACHING_REDIS_PASSWORD:
        REDIS_CACHE_CON_STRING = f"{REDIS_CACHE_CON_STRING}:{CACHING_REDIS_PASSWORD}@"
    REDIS_CACHE_CON_STRING = f"{REDIS_CACHE_CON_STRING}{CACHING_REDIS_HOST}:{CACHING_REDIS_PORT}/{CACHING_REDIS_DATABASE}"
    CACHEOPS_REDIS = REDIS_CACHE_CON_STRING

CACHEOPS_ENABLED = bool(CACHE_TIMEOUT)
CACHEOPS_DEFAULTS = {"timeout": CACHE_TIMEOUT}
CACHEOPS = {
    "auth.user": {"ops": "get", "timeout": 900},
    "auth.*": {"ops": ("fetch", "get")},
    "auth.permission": {"ops": "all"},
    "devices.*": {"ops": "all"},
    "net.*": {"ops": "all"},
    "peering.*": {"ops": "all"},
    "peeringdb.*": {"ops": "all"},
    "users.*": {"ops": "all"},
    "utils.*": {"ops": "all"},
    "webhooks.*": {"ops": "all"},
}
CACHEOPS_DEGRADE_ON_FAILURE = True

if TASKS_REDIS_USING_SENTINEL:
    RQ_PARAMS = {
        "SENTINELS": TASKS_REDIS_SENTINELS,
        "MASTER_NAME": TASKS_REDIS_SENTINEL_SERVICE,
        "DB": TASKS_REDIS_DATABASE,
        "PASSWORD": TASKS_REDIS_PASSWORD,
        "SOCKET_TIMEOUT": None,
        "CONNECTION_KWARGS": {"socket_connect_timeout": TASKS_REDIS_DEFAULT_TIMEOUT},
    }
else:
    RQ_PARAMS = {
        "HOST": TASKS_REDIS_HOST,
        "PORT": TASKS_REDIS_PORT,
        "DB": TASKS_REDIS_DATABASE,
        "PASSWORD": TASKS_REDIS_PASSWORD,
        "DEFAULT_TIMEOUT": TASKS_REDIS_DEFAULT_TIMEOUT,
        "SSL": TASKS_REDIS_SSL,
    }
RQ_QUEUES = {"default": RQ_PARAMS, "check_releases": RQ_PARAMS}


# Email
if EMAIL:
    EMAIL_HOST = EMAIL.get("SERVER")
    EMAIL_PORT = EMAIL.get("PORT", 25)
    EMAIL_HOST_USER = EMAIL.get("USERNAME")
    EMAIL_HOST_PASSWORD = EMAIL.get("PASSWORD")
    EMAIL_TIMEOUT = EMAIL.get("TIMEOUT", 10)
    SERVER_EMAIL = EMAIL.get("FROM_ADDRESS")
    EMAIL_SUBJECT_PREFIX = EMAIL.get("SUBJECT_PREFIX")
    EMAIL_USE_SSL = EMAIL.get("USE_SSL")
    EMAIL_USE_TLS = EMAIL.get("USE_TLS")
    EMAIL_SSL_KEYFILE = EMAIL.get("SSL_KEYFILE")
    EMAIL_SSL_CERTFILE = EMAIL.get("SSL_CERTFILE")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cacheops",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "netfields",
    "taggit",
    "devices",
    "extras",
    "net",
    "peering",
    "peeringdb",
    "users",
    "utils",
    "webhooks",
    "django_rq",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "utils.middleware.RequireLoginMiddleware",
    "utils.middleware.ExceptionCatchingMiddleware",
    "utils.middleware.ObjectChangeMiddleware",
    "users.middleware.LastSearchMiddleware",
]

# Prometheus setup
if METRICS_ENABLED:
    PROMETHEUS_EXPORT_MIGRATIONS = False
    INSTALLED_APPS.append("django_prometheus")
    MIDDLEWARE = (
        ["django_prometheus.middleware.PrometheusBeforeMiddleware"]
        + MIDDLEWARE
        + ["django_prometheus.middleware.PrometheusAfterMiddleware"]
    )
    configuration.DATABASE.update(
        {"ENGINE": "django_prometheus.db.backends.postgresql"}
    )

if DEBUG:
    # Enable debug toolbar only in debugging mode
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

ROOT_URLCONF = "peering_manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "utils.context_processors.settings",
                "utils.context_processors.affiliated_autonomous_systems",
            ]
        },
    }
]

WSGI_APPLICATION = "peering_manager.wsgi.application"


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Authentication URL
LOGIN_URL = f"/{BASE_PATH}login/"


# Messages
MESSAGE_TAGS = {messages.ERROR: "danger"}


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = f"/{BASE_PATH}static/"
STATICFILES_DIRS = (BASE_DIR / "project-static",)

# Django debug toolbar
INTERNAL_IPS = ["127.0.0.1", "::1"]
