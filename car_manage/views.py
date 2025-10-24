from django.shortcuts import render
from car_manage.models import Car # Use the ORM from Django to access the DB via class

############### USER VIEW - ###################

def car_view(request):
  db_cars = Car.objects.all() # Get all the info from the db cars
  search = request.GET.get('search') # custom search via url
  
  #if is being user, show specific model. Else render all cars
  if search:
    db_cars = db_cars.filter(model__contains = search)
  
  
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
  
  