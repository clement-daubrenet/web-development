from django.db import models

class Sites(models.Model):
	
    site_name =  models.CharField(max_length=200,default="-")

class Values(models.Model):

    site =  models.ForeignKey('Sites')
    date =  models.DateField(default="-")
    value_a = models.FloatField(default=0)
    value_b = models.FloatField(default=0)