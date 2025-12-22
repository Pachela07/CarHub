from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from django.http import HttpRequest, HttpResponse
from tkinter import messagebox

## Register a new user using the predefined UserCreationForm build in Django
def new_register(request: HttpRequest) -> HttpResponse:
    # Handle user registration with Django's built-in form
    if request.method == "POST":
        register_new_user = UserCreationForm(request.POST)
        if register_new_user.is_valid():
            register_new_user.save()
            return redirect('login')
        # If the form is invalid, it will fall through and re-render below
    else:
        register_new_user = UserCreationForm()

    return render(
        request,
        'register.html',
        {'register_new_user': register_new_user},
    )
## Creat a new user, do proper validations using authenticate and login, show a warmingbox if the info is not valid.
def new_login(request ) :
    if request.method == "POST":
        # Capture the info from the user
        username = request.POST["username"]
        password = request.POST["password"]
        
        #Auth if the user is valid in the db
        user = authenticate(
            request, 
            username= username,
            password=password)
        #Check if the login is valid and redirect
        if user is not None:
            login(request, user)
            return redirect('index')
        #Return to the login if invalid
        else:
            #Show a simple messagebox using tkinter
            messagebox.showwarning("Info", "The data that you have provided is not valid")
            user_login = AuthenticationForm()
            
    else:
        user_login = AuthenticationForm()
    return render(
                request,
                'login.html',
                {'user_login': user_login},
    )

## Logout the user 
def new_logout(request):
    logout(request)
    return redirect('index')