from django.shortcuts import render
from weather.models import City

# Create your views here.

def index(request):
    cities_data = City.objects.all()
    cities_dictionary={}
    for unique_city in cities_data:
        cities_dictionary[unique_city.city_id] = unique_city.city_name
    template_name='base.html'
    return render(request,template_name,{"cities_dictionary": cities_dictionary})
