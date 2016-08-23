from django.db import models

class Sites(models.Model):
	"""
	This model is for websites names and ids.
	n.b: primary key is set up automatically.
	"""
	site_name =  models.CharField(max_length=200,default="-")

class Values(models.Model):
	"""
	This model is for the date and the values 
	for a given website. 
	"""
	site =  models.ForeignKey('Sites')
	date =  models.DateField(default="-")
	value_a = models.FloatField(default=0)
	value_b = models.FloatField(default=0)