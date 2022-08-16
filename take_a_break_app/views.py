from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
import requests
from requests import request
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from take_a_break_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import serializers
import logging
import datetime
import re

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

def main(request, guest):
    message = ""
    if (request.method == "POST"):
        form = forms.take_a_break(request.POST)
        if form.is_valid():
            time = form.cleaned_data["time"]
            website = form.cleaned_data["website"]
            request.session["website"] = website
            if valid_take_a_break_format(website):
                return HttpResponseRedirect(reverse("take_a_break_app:break", kwargs={"time": time}))
            else:
                message = "please select a website"
    
    if (guest):
        return render(request, "take_a_break_app/main.html", {
            "message": message
        })
    try:
        list_of_web_id = get_all_website_id(request.session["username"])
        list_of_websites = []
        for web_id in list_of_web_id:
            website = Websites.objects.get(pk=web_id)
            list_of_websites.append(website)
        if len(list_of_websites) == 0:
            list_of_websites = None
        return render(request, "take_a_break_app/main.html", {
            "username" : request.session["username"],
            "list_of_websites" : list_of_websites,
            "message": message
        })
    except KeyError:
        # if no user info
        return render(request, "take_a_break_app/main.html", {
            "message": message
        })

def take_a_break(request, time):
    return render(request, "take_a_break_app/take_a_break.html", {
        "website": request.session["website"],
        "time": time, 
        "host": request.get_full_path()
    })

def add(request, guest):
    if (request.method == "POST"):
        form = forms.add_web(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            url = form.cleaned_data["url"]
            response_code = valid_website(url)
            message = ""
            if response_code == 0:
                create_websites(request.session["username"], name, url)
                message = "add successfully"
            elif response_code == 1:
                message = "please enter full url"
            elif response_code == 2:
                message = "Can not find this website"
            elif response_code == 3:
                message = "Please no not take a break in this website"
            elif response_code == 4:
                message = "the length of the url is too long"
            elif len(name)> 900:
                message = "the length of the name is too long"
            return render(request, "take_a_break_app/add.html", {
                    "username" : request.session["username"],
                    "message": message
                })
    if (guest):
        return render(request, "take_a_break_app/add.html", {
        })
    else:
        try:
            return render(request, "take_a_break_app/add.html", {
                "username" : request.session["username"],
            })
        except KeyError:
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
            return HttpResponseRedirect(reverse("take_a_break_app:start"))
        elif response_id == 1:
            error_message = "Please enter valid character"
        elif response_id == 2:
            error_message = "Please double check your password"
        elif response_id == 3:
            error_message =  "User already exist"
        elif response_id == 4:
            error_message = "Username is too long"
        elif response_id == 5:
            error_message = "Email is too long"
        elif response_id == 6:
            error_message = "Password is too long"
        elif response_id == 7:
            error_message = "Incorrect email format"
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



# all helpers

def valid_take_a_break_format(website):
    if website == "defalut":
        return False
    else:
        return True

def valid_website(website):
    '''
    0: All good
    1: not full url (missing http header)
    2: can't find website
    3: link to website itself
    4. length too long
    '''
    if (website.startswith("https://") or website.startswith("http://")):
        if len(website) > 900:
            return 4
        if website.startswith("https://take-a-break-app.herokuapp.com/"):
            return 3
        try:
            response = requests.get(website)
            if response.status_code == 200:
                return 0
            else: 
                return 2
        except:
            return 2
    else:
        return 1
        

def valid_user_register_format(form):
    '''
    0: All good
    1: invalid form
    2: different password and confirm password
    3: user_already exist
    4: username or password or email is too long
    '''
    if form.is_valid():
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        confirmed_password = form.cleaned_data["confirm_password"]
        if (password != confirmed_password):
            return 2
        if len(username)> 100:
            return 4
        if len(email)> 100:
            return 5
        pattern = "^\S+@\S+\.\S+$"
        if len(password)> 100:
            return 6
        if not check_user_exist(username):
            return 3 
        if not valid_email(email):
            return 7
        return 0
    else:
        return 1

def valid_email(email):
    pattern = "^\S+@\S+\.\S+$"
    objs = re.search(pattern, email)
    try:
        if objs.string == email:
            return True
    except:
        return False

# check if user exist already
def check_user_exist(username):
    try:
        User.objects.get(username=username)
        return False
    except User.DoesNotExist:
        return True

def create_websites(username, name, url):
    try:
        web = Websites.objects.get(name=name, url=url)
    except Websites.DoesNotExist:
        web = Websites.objects.create(name=name, url=url)
    user = User.objects.get(username=username)
    User_web.objects.get(user=user).websites.add(web)
    

def get_all_website_id(username):
    user=User.objects.get(username=username)
    list_of_webs = list(User_web.objects.get(user=user).websites.all())
    web_pks = []
    for web in list_of_webs:
        web_pks.append(web.id)
    return web_pks

def log(message):
    logger = logging.getLogger(__name__)
    message = datetime.datetime.now().strftime("[%d/%b/%Y %X] ") + str(message)
    logger.critical(message)


    
