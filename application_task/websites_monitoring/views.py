# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = 'websites_monitoring/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context

class SitesView(TemplateView):
    template_name = 'websites_monitoring/sites.html'

class SummaryView(TemplateView):
    template_name = 'websites_monitoring/summary.html'