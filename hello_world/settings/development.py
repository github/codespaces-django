from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1"]

# Support for GitHub Codespaces
if 'CODESPACE_NAME' in os.environ:
    from decouple import config
    codespace_name = config("CODESPACE_NAME")
    domain = config("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")
    codespace_host = f"{codespace_name}-8000.{domain}"
    ALLOWED_HOSTS.append(codespace_host)
    CSRF_TRUSTED_ORIGINS.append(f"https://{codespace_host}")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "OPTIONS": {
            "timeout": 20,
        },
    }
}

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
