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
from websites_monitoring.views import HomePageView, DynamicSiteView, SitesView, SummaryViewAverage, SummaryViewSum

urlpatterns = [
    url(r'^$', SitesView, name='sites'),
    url(r'^sites/([0-9]{1})', DynamicSiteView, name='dynamic_site_view'),
    url(r'^sites', SitesView, name='sites'),
    url(r'^summary-average/', SummaryViewAverage, name='summary-average'),
    url(r'^summary', SummaryViewSum, name='summary')
]
