from django.shortcuts import render
from car_manage.models import Car # Use the ORM from Django to access the DB via class

############### USER VIEW - ###################

def car_view(request):
  db_cars = Car.objects.all().order_by('model') # Get all the info from the db cars and order by model
  search = request.GET.get('search') # custom search via url
  
  #if 'search' is being used, show specific model. Else render all cars in the db
  if search:
    db_cars = db_cars.filter(model__icontains = search)
  
################# RETURN THE CONTENT ##################  
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
  
  