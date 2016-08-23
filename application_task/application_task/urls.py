"""application_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from websites_monitoring.views import general_sites_view, \
    particular_site_view, summary_average_view, summary_sum_view

urlpatterns = [
    url(r'^$', general_sites_view, name='home'),
    url(r'^sites/([0-9]{1})', particular_site_view, name='particular-site'),
    url(r'^sites', general_sites_view, name='general-sites'),
    url(r'^summary-average', summary_average_view, name='summary-average'),
    url(r'^summary', summary_sum_view, name='summary-sum')
]
