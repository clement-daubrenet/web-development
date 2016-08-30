from __future__ import unicode_literals

from django.db import models

class City(models.Model):
    """
    City ids and names taken from external weather API.
    e.g : weather.com/forecast.io
    """
    city_id          =  models.IntegerField(default="0", primary_key=True)
    city_name        =  models.CharField(max_length=200,default="-")

class Forecast(models.Model):
    """
    Forecasts for the upcomming 6 days for the cities
    of the city table.
    e.g : forecast_1 : day1, forecast_2 : day2
    """
    city           =  models.ForeignKey('City')
    forecast_1     =  models.CharField(max_length=200,default="-")
    forecast_2     =  models.CharField(max_length=200,default="-")
    forecast_3     =  models.CharField(max_length=200,default="-")
    forecast_4     =  models.CharField(max_length=200,default="-")
    forecast_5     =  models.CharField(max_length=200,default="-")
    forecast_6     =  models.CharField(max_length=200,default="-")
    
class Temperature(models.Model):
    """
    Temperature on average (in Farenheit) for the 
    upcomming 6  days in the cities of the city table.
    """
    city                      =  models.ForeignKey('City')
    average_temperature_1     =  models.FloatField(default="-")
    average_temperature_2     =  models.FloatField(default="-")
    average_temperature_3     =  models.FloatField(default="-")
    average_temperature_4     =  models.FloatField(default="-")
    average_temperature_5     =  models.FloatField(default="-")
    average_temperature_6     =  models.FloatField(default="-")
