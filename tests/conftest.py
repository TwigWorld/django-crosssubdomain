import django
from django.conf import settings


def pytest_configure(config):
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        INSTALLED_APPS=["crosssubdomain"],
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'crosssubdomain.context_processors.document_domain',
                    ],
                    "debug": True,  # We want template errors to raise
                }
            },
        ],
    )
    django.setup()
