from django.http import HttpResponse
from django.shortcuts import render
from . import database
from . import forms

# Create your views here.



def start(request):
    return render(request, "take_a_break_app/start.html", {
        "website": range(1, 5)
    })

def still_building(request):
    return render(request, "take_a_break_app/still_building.html")

def main(request):
    return render(request, "take_a_break_app/main.html", {
        "website": range(1, 5)
    })

def register(request):
    if (request.method == "POST"):
        form = forms.User_info(request.POST)
        response_id = valid_username_format(form)
        if response_id == 0:
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            database.create_user(username, email, password)
            return render(request, "take_a_break_app/register_complete.html", {
                "username": username,
                "email": email,
                "password": password,
            })
        elif response_id == 1:
            return render(request, "take_a_break_app/register.html", {
                "user_form": form,
                "message": "Please enter valid character",
            })
        elif response_id == 2:
             return render(request, "take_a_break_app/register.html", {
                "user_form": form,
                "confirm_password_message": "Please double check your password",
            })
    else:
        return render(request, "take_a_break_app/register.html", {
            "user_form": forms.User_info()
        }) 

def register_complete(request):
    
    return render(request, "take_a_break_app/register_complete.html", {
            "username": "username",
            "email": "email",
            "password": "password",
        })

def valid_username_format(form):
    '''
    0: All good
    1: invalid form
    2: different password and confirm password
    '''
    if form.is_valid():
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        confirmed_password = form.cleaned_data["confirm_password"]
        if (password != confirmed_password):
            return 2
        return 0
    else:
        return 1

    