INSTALLED_APPS = [
    "sample.groups",
    "sample.networks",
]

SECRET_KEY = "test"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
