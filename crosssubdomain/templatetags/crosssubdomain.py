from django import template
from django.conf import settings
from django.utils.html import mark_safe


def get_document_domain():
    domain = getattr(settings, "JS_DOCUMENT_DOMAIN", None)
    return domain if domain is not None else ""


def set_document_domain():
    domain = get_document_domain()
    if domain != "":
        return mark_safe(
            f'<script type="text/javascript">document.domain="{domain}";</script>'
        )
    return ""


register = template.Library()

register.simple_tag(get_document_domain)
register.simple_tag(set_document_domain)
