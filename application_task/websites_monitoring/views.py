# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from collections import OrderedDict
from django.db.models import Sum
import websites_monitoring.models as monitoring

def general_sites_view(request):
    """
    This view is rendering the different websites ids and names. 
    e.g : {"1": "Demo Site", "2": "ABC Site", ...}  
    """
    template_name = 'websites_monitoring/sites.html'
    sitesbaselist = monitoring.Sites.objects.all()
    dict_of_sites = {}
    for site in sitesbaselist:
        dict_of_sites[site.id] = site.site_name
    return render(request, template_name, {"dict_of_sites" : dict_of_sites})

def particular_site_view(request, site_id):
    """
    This view is rendering the values for a given website. 
    e.g : {"2015-02-03": {"a": 20.00, "b": 100.00}, ...}
    """
    summarylist = monitoring.Values.objects.filter(site_id=site_id)
    date_values_dictionnary = OrderedDict()
    for report in summarylist: 
        date_values_dictionnary[report.date] =  {"a" : report.value_a, "b" : report.value_b}
    template_name = 'websites_monitoring/specific_site.html'
    return render(request, template_name, {"date_values_dictionnary" : date_values_dictionnary})


def summary_average_view(request):
    """
    This view is rendering the average of each value
    for the different websites.
    e.g :  {"Demo Site" : {'a' : 20.00, 'b' : 100.00}, ...}
    n.b : This method uses python code only to compute the 
    averages as asked in the task description.
    """
    template_name = 'websites_monitoring/summary-average.html'
    sitesbaselist = monitoring.Sites.objects.all()
    dict_of_averages = OrderedDict()
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

def summary_sum_view(request):
    """
    This view is rendering the sum of each value
    for the different websites.
    e.g :  {"Demo Site" : {'a' : 20.00, 'b' : 100.00}, ...}
    n.b : This method is based on Django SQL layer to compute 
    the sums as asked in the task description.
    """
    sitesbaselist = monitoring.Sites.objects.all()
    sums = map(lambda site_id : {site_id.site_name : monitoring.Values.objects.filter(site_id=site_id).aggregate(Sum('value_a'), Sum('value_b'))}, monitoring.Sites.objects.all())    
    template_name = 'websites_monitoring/summary.html'
    return render(request, template_name, {"result_sums" : sums})
