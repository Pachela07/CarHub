from django.shortcuts import render
from car_manage.models import Car # Use the ORM from Django to access the DB via class

############### USER VIEW - ###################

def car_view(request):
  
  db_cars = Car.objects.all() # get all the info from the db cars
  
  
  
  return render(
    request,
    'cars.html',
    {'db_cars' : db_cars} 
    ) # use the default request and the template page you want to get

def index(request):
  return render(
    request,
    'index.html'
  ) # default page just for test purposes 
  
  