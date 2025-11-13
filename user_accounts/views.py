from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 

def new_user_view(request):
  new_user_form = UserCreationForm()
  return render(
    request,
    'new_user.html',
    {'new_user_form' : new_user_form}
  )
  
  