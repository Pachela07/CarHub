############### IMPORTS - ###################
from django.shortcuts import render,redirect # Shortcut to return an HTML response
from car_manage.models import Car # Use the ORM from Django to access the DB via class
from car_manage.forms import CarForm # Import the predefined form

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
  
############### USER VIEW// RETURN THE CONTENT - ###################
  
def new_car_view(request):
    return render(
    request,
    'new_car.html')
    # if you forget the render the PATH will overload
    
def add_new_car(request):
  ## Check if the user is filled or not and apply the specific request
  if request.method == 'POST':
    new_form = CarForm(request.POST, request.FILES) # new form filled after the method has been checked, and accept files in the second request
    if new_form.is_valid(): # Check if the form is valid with the correct data
      new_form.save() # Save it using the method created iin the forms.py
      return redirect('index') # return to the main page
    else:
      # Return the same page with validation errors so the user can correct them
      return render(request, 'new_car.html', { 'new_form' : new_form })
  else:
    new_form = CarForm()
    return render(request, 'new_car.html', # Renders the page
              { 'new_form' : new_form}) # Loads the form with empty details

################# DUMMY/TESTS ##################  
def skeleton(request):
  return render(
    request,
    'skeleton.html'
  ) # default page 
  
  