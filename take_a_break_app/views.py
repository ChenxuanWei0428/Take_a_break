from django.http import HttpResponse
from django.shortcuts import render
from . import database 
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.



def start(request):
    if request.method == "post":
        form = forms.User_info(request.POST)
    else:
        return render(request, "take_a_break_app/start.html", {
        })

def still_building(request):
    return render(request, "take_a_break_app/still_building.html")

def main(request):
    return render(request, "take_a_break_app/main.html", {
        "user": "test",
    })

def recover_account(request):
    pass

def register(request):
    if (request.method == "POST"):
        form = forms.User_info(request.POST)
        response_id = valid_username_format(form)
        error_message = ""
        if response_id == 0:
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if database.create_user(username, email, password):
                # go back to start
                return render(request, "take_a_break_app/register_complete.html", {
                    "username": username,
                    "email": email,
                    "password": password,
                })
            else:
                return render(request, "take_a_break_app/register.html", {
                "user_form": form,
                "message": "Database did not work correctly",
            })
        elif response_id == 1:
            error_message = "Please enter valid character"
        elif response_id == 2:
            error_message = "Please double check your password"
        elif response_id == 3:
            error_message =  "User already exist"
        return render(request, "take_a_break_app/register.html", {
                "user_form": form,
                "error_message": error_message,
        })
    else:
        return render(request, "take_a_break_app/register.html") 

def register_complete(request):
    
    return render(request, "take_a_break_app/register_complete.html", {
            "username": "username",
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
        if not database.check_user_exist(username):
            return 3 
        return 0
    else:
        return 1

    