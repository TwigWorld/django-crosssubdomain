from django import test
from django.template import Template, Context

import context_processors


class MenuTestCase(test.TestCase):

    def setUp(self):
        self.context = Context({})
        self.get_template = Template("{% load crosssubdomain %}{% get_document_domain %}")
        self.set_template = Template("{% load crosssubdomain %}{% set_document_domain %}")

    def test_with_domain(self):

        with self.settings(JS_DOCUMENT_DOMAIN='testdomain'):

            request = test.RequestFactory()
            context = context_processors.document_domain(request)

            self.assertEquals(
                context['js_document_domain'],
                'testdomain'
            )

            self.assertEquals(
                self.get_template.render(self.context),
                'testdomain'
            )

            self.assertEquals(
                self.set_template.render(self.context),
                '<script type="text/javascript">document.domain="testdomain";</script>'
            )

    def test_without_domain(self):

        request = test.RequestFactory()
        context = context_processors.document_domain(request)

        self.assertEquals(
            context['js_document_domain'],
            None
        )

        self.assertEquals(
            self.get_template.render(self.context),
            ''
        )

        self.assertEquals(
            self.set_template.render(self.context),
            ''
        )
