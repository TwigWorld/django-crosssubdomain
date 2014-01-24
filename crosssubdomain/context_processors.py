from django.conf import settings


def document_domain(request):
    """
    Provide the JavaScript domain setting to the context, or None if not set
    """
    return {
        'js_document_domain': getattr(settings, 'JS_DOCUMENT_DOMAIN', None)
    }
