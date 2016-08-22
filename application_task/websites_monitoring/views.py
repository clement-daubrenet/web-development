# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import render
from collections import OrderedDict
import websites_monitoring.models as monitoring
import math

class HomePageView(TemplateView):
    template_name = 'websites_monitoring/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context

def SitesView(request):
    sitesbaselist = monitoring.Sites.objects.all()
    dict_of_sites = {}
    for site in sitesbaselist:
        dict_of_sites[site.id] = site.site_name
    template_name = 'websites_monitoring/sites.html'

    return render(request, template_name, {"dict_of_sites" : dict_of_sites})

def SummaryViewAverage(request):
    sitesbaselist = monitoring.Sites.objects.all()
    dict_of_averages = OrderedDict()
    template_name = 'websites_monitoring/summary-average.html'
    for site in sitesbaselist:
        counter, count_a_values, count_b_values = (0, 0, 0)
        summarylist = monitoring.Values.objects.filter(site_id=site.id)
        for report in summarylist:
            counter += 1 
            count_a_values += report.value_a
            count_b_values += report.value_b

        average_a_value = '%.2f' % float((count_a_values)/counter)
        average_b_value = '%.2f' % float((count_b_values)/counter)
        dict_of_averages[site.site_name] = {'a' : average_a_value, 'b' : average_b_value}
    return render(request, template_name,{"result_dict" : dict_of_averages})

def SummaryViewSum(request):
    sitesbaselist = monitoring.Sites.objects.all()
    dict_of_sums = OrderedDict()
    template_name = 'websites_monitoring/summary.html'
    for site in sitesbaselist:
        counter, count_a_values, count_b_values = (0, 0, 0)
        summarylist = monitoring.Values.objects.filter(site_id=site.id)
        for report in summarylist:
            counter += 1 
            count_a_values += report.value_a
            count_b_values += report.value_b

        sum_a_values = '%.2f' % count_a_values
        sum_b_values = '%.2f' % count_b_values
        dict_of_sums[site.site_name] = {'a' : sum_a_values, 'b' : sum_b_values}
    return render(request, template_name,{"result_dict" : dict_of_sums})

def DynamicSiteView(request, site_id):
    summarylist = monitoring.Values.objects.filter(site_id=site_id)
    date_values_dictionnary = OrderedDict()
    for report in summarylist: 
        date_values_dictionnary[report.date] =  {"a" : report.value_a, "b" : report.value_b}
    template_name = 'websites_monitoring/specific_site.html'
    print date_values_dictionnary
    return render(request, template_name, {"date_values_dictionnary" : date_values_dictionnary})