INSTALLED_APPS = ["sample.groups", "sample.networks"]
SECRET_KEY = "public-repro-only-not-for-production"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
