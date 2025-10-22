from django.shortcuts import render

############### USER VIEW - ###################

def car_view(request):
  return render(request, 'index.html') # use the default request and the template page you want to get
