from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from take_a_break_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import serializers
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
                request.session["username"] = username
                list_of_webs = list(User_web.objects.get(user=user).websites.all())
                web_pks = []
                for web in list_of_webs:
                    web_pks.append(web.id)
                request.session["list_of_webs"] = web_pks
                return HttpResponseRedirect(reverse("take_a_break_app:main"))
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
    list_of_web_id = request.session["list_of_webs"]
    list_of_websites = []
    for web_id in list_of_web_id:
        website = Websites.objects.get(pk=web_id)
        list_of_websites.append(website)
    return render(request, "take_a_break_app/main.html", {
        "username" : request.session["username"],
        "list_of_websites" : list_of_websites,
        "index": 0
    })

def add(request):
    return render(request, "take_a_break_app/add.html", {

    })

def recover_account(request):
    pass

def register_user(request):
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
            User_web.objects.create(user=user)
            return HttpResponseRedirect(reverse("take_a_break_app:main"), kwargs={"username": username})
        elif response_id == 1:
            error_message = "Please enter valid character"
        elif response_id == 2:
            error_message = "Please double check your password"
        elif response_id == 3:
            error_message =  "User already exist"
        log(error_message)
        return render(request, "take_a_break_app/register.html", {
                "user_form": form, #todo, add value back
                "error_message": error_message,
        })
    else:
        return render(request, "take_a_break_app/register.html") 

def register_complete(request, username):
    return render(request, "take_a_break_app/register_complete.html", {
        "username": username,
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

def create_websites(username, name, url):
    web = Websites.objects.get(name=name, url=url)
    if web is None:
        web = Websites.objects.create(name=name, url=url)
    user = User.objects.get(username=username)
    User_web.objects.get(user=user).websites.add(web)
    

def log(message):
    logger = logging.getLogger(__name__)
    message = datetime.datetime.now().strftime("[%d/%b/%Y %X] ") + str(message)
    logger.critical(message)


    
