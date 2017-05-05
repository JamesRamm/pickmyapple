from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page

from market.models import MarketItem


class HomePage(Page):
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)

        context['offers'] = MarketItem.objects.all()
        return context
