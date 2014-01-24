django-crosssubdomain
=====================

A small Django application for providing templates with a document.domain
setting for cross-subdomain JavaScript

Simply add JS_DOCUMENT_DOMAIN to your Django settings and set it to the common
domain that you want your JavaScript applications to share, e.g.

```python

JS_DOCUMENT_DOMAIN = 'djangoproject.com'

```

Django Cross-Subdomain can be used both as a loosely-coupled (optional)
application and as a strongly coupled (required) application.


Loosely coupled API
-------------------

If you can't guarantee that Django Cross-Subdomain will be installed within a
project, but you still want your Django application to support it if present,
then you can take advantage of the context_processor, which simply updates
the context with the variable js_document_domain, if present.

Use it as follows:

```html

{% if js_document_domain %}
    <script type="text/javascript">document.domain = "{{ js_document_domain }}";</script>
{% endif %}

```

Then, as long as the project sets JS_DOCUMENT_DOMAIN, includes 'crosssubdomain'
in INSTALLED_APPS, and includes 'crosssubdomain.context_processors.document_domain'
in TEMPLATE_CONTEXT_PROCESSORS, the tag will execute. Otherwise, nothing happens
and no error is raised - unless of course js_document_domain has been added to
the context in some other way.


Strongly coupled API
--------------------

If you know that your project includes Django Cross-Subdomain, then you can
use its templatetags in your templates instead:

```html

{% load crosssubdomain %}

```

The following template tags are available:

##get_document_domain

Provides the JS_DOCUMENT_DOMAIN setting as a string (or None).

```html

{% get_document_domain %}  <!-- 'djangoproject.com' -->

```


##set_document_domain

If JS_DOCUMENT_DOMAIN is set, then this tag will insert the necessary script
element directly into the DOM.

```html

{% set_document_domain %} <!-- <script type="text/javascript">document.domain="djangoproject.com";</script>

```
