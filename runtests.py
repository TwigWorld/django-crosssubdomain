from django.conf import settings
from django.core.management import call_command

settings.configure(

    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    INSTALLED_APPS=(
        'crosssubdomain',
    ),
    TEMPLATE_CONTEXT_PROCESSORS=(
        'crosssubdomain.context_processors.document_domain',
    )
)

call_command('test')
