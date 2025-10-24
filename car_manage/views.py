from django.shortcuts import render
from car_manage.models import Car # Use the ORM from Django to access the DB via class

############### USER VIEW - ###################

def car_view(request):
# search = request.GET.get('search')
  db_cars = Car.objects.all() # Get all the info from the db cars
  
# filtered_cars = Car.objects.filter(brand__name = 'example') # Filter by a specific value withou using the ID
# filtered_cars = Car.objects.filter(model__contains = 'search') # Filter by a specific string
  
  
  
  return render(
    request,
    'index.html',
    {'db_cars' : db_cars} 
    ) # use the default request and the template page you want to get

def skeleton(request):
  return render(
    request,
    'skeleton.html'
  ) # default page just for test purposes 
  
  