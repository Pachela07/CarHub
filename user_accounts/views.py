from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):

    if request.method == "POST":
        # Bind POST data to the form (includes username and password fields)
        register_new_user = UserCreationForm(request.POST)

        if register_new_user.is_valid():
            # Save creates the user in the database
            register_new_user.save()

            # On success, redirect the user to the homepage 
            return redirect('index')
    else:
            # If the form is invalid, render the template again with:
            # - the bound form (so the user sees their inputs and error messages)
        register_new_user = UserCreationForm()
        return render(
                request,
                'new_user.html',
                {'register_new_user': register_new_user},
            )