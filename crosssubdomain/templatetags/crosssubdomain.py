from django import template
from django.conf import settings


def get_document_domain():
    domain = getattr(settings, 'JS_DOCUMENT_DOMAIN', None)
    return domain if domain is not None else ''


def set_document_domain():
    domain = get_document_domain()
    if domain != '':
        return u'<script type="text/javascript">document.domain="{domain}";</script>'.format(
            domain=domain
        )
    return ''


register = template.Library()

register.simple_tag(get_document_domain)
register.simple_tag(set_document_domain)
