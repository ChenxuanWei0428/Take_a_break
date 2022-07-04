from dataclasses import dataclass
from distutils.log import error
from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from take_a_break_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import logging
import datetime

def start(request):
    error_message = ""
    if (request.method == "POST"):
        form = forms.User_login(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                return render(request, "take_a_break_app/main.html", {
                    "username": username,
                })
            else:
                error_message = "Unauthrized login"
        else:
            error_message = "not valid from format"
    log(error_message)
    return render(request, "take_a_break_app/start.html", {
        "error_message": error_message
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
        response_id = valid_user_register_format(form)
        error_message = ""
        if response_id == 0:
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, email, password)
            user.save()
            return render(request, "take_a_break_app/register_complete.html", {
                "username": username,
                "email": email,
                "password": password,
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

def valid_user_register_format(form):
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
        if not check_user_exist(username):
            return 3 
        return 0
    else:
        return 1

def check_user(username, password):
    pass
# check if user exist already
def check_user_exist(username):
    try:
        User.objects.get(username=username)
        return False
    except User.DoesNotExist:
        return True

def create_websites(name, url):
    pass

def log(message):
    logger = logging.getLogger(__name__)
    message = datetime.datetime.now().strftime("[%d/%b/%Y %X] ") + message
    logger.critical(message)