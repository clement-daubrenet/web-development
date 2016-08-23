# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from collections import OrderedDict
from django.db.models import Sum, DecimalField
from decimal import *
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
    return render(request, template_name, {"dict_of_sites": dict_of_sites})


def particular_site_view(request, site_id):
    """
    This view is rendering the dates/values for a given
    website.
    e.g for key "site_name":
    "Demo Site"
    e.g for key "date_value_dictionary":
    {"2015-02-03": {"a": 20.00, "b": 100.00}, ...}
    """
    template_name = 'websites_monitoring/specific-site.html'
    summarylist = monitoring.Values.objects.filter(site_id=site_id)
    particular_site = monitoring.Sites.objects.filter(id=site_id)[0]
    date_values_dictionnary = OrderedDict()
    for report in summarylist:
        date_values_dictionnary[report.date] = \
            {"a": '%.2f' % report.value_a, "b": '%.2f' % report.value_b}
    return render(request,
                  template_name,
                  {"site_name": particular_site.site_name,
                   "date_values_dictionnary": date_values_dictionnary})


def summary_average_view(request):
    """
    This view is rendering the average of each value
    for the different websites.
    e.g :  {"Demo Site" : {'a' : 17.33, 'b' : 55.33}, ...}
    n.b : This method uses python code only to compute the
    averages as asked in the task description.
    """
    template_name = 'websites_monitoring/summary-average.html'
    sites = monitoring.Sites.objects.all()
    averages = OrderedDict()
    for site in sites:
        counter, count_a_values, count_b_values = (0, 0, 0)
        summarylist = monitoring.Values.objects.filter(site_id=site.id)
        for report in summarylist:
            counter += 1
            count_a_values += report.value_a
            count_b_values += report.value_b

        average_a_value = '%.2f' % float((count_a_values)/counter)
        average_b_value = '%.2f' % float((count_b_values)/counter)
        averages[site.site_name] = {'value_a': average_a_value,
                                    'value_b': average_b_value}
    return render(request, template_name, {"result_dict": averages})


def summary_sum_view(request):
    """
    This view is rendering the sum of each value
    for the different websites.
    e.g :  {"Demo Site" : {'a' : 52.00, 'b' : 196.00}, ...}
    n.b : This method is based on Django SQL layer to compute
    the sums as asked in the task description.
    """
    template_name = 'websites_monitoring/summary.html'
    sites = monitoring.Sites.objects.all()
    values = monitoring.Values.objects.all()
    sums = map(
        lambda site: {
            site.site_name:
            values.filter(site_id=site).aggregate(
                Sum('value_a',
                    output_field=DecimalField(decimal_places=2)),
                Sum('value_b',
                    output_field=DecimalField(decimal_places=2)))}, sites)

    template_name = 'websites_monitoring/summary.html'
    return render(request, template_name, {"result_dict": sums})
