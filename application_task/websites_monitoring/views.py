# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import render

import websites_monitoring.models as monitoring

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

def SummaryView(request):
    sitesbaselist = monitoring.Sites.objects.all()
    dict_of_averages = {}
    template_name = 'websites_monitoring/summary.html'
    for site in sitesbaselist:
        counter, count_a_values, count_b_values = (0, 0, 0)
        summarylist = monitoring.Values.objects.filter(site_id=site.id)
        for report in summarylist:
            counter += 1 
            count_a_values += report.value_a
            count_b_values += report.value_b

        average_a_value = float(count_a_values)/counter
        average_b_value = float(count_b_values)/counter
        dict_of_averages[site.site_name] = {'average_a' : average_a_value, 'average_b' : average_b_value}
    return render(request, template_name,{"dict_of_averages" : dict_of_averages})

def SummaryViewSum(request):
    pass
        



# def index(request):

#   dictionary_of_cities_forecast = {}
#   dictionary_of_cities_temperature = {}
#   citybaselist=weatherbase.City.objects.all()


#   for wb in citybaselist:
#       forecast_city = weatherbase.Forecast.objects.get(city_id=wb.city_id)
#       temperature_city = weatherbase.Temperature.objects.get(city_id=wb.city_id)
#       dictionary_of_cities_forecast[wb.city_name] = forecast_city.forecast_1
#       dictionary_of_cities_temperature[wb.city_name] = temperature_city.average_temperature_1

#   return render(request, 'index.html', {"dict_forecast" : dictionary_of_cities_forecast})
