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
    return render(request, "take_a_break_app/register.html")

def register_complete(request):
    if (request.method == "POST"):
        form = forms.Userinfo(request.POST)
        if valid_username_format(form):
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            return render(request, "take_a_break_app/register_complete.html", {
                "username": username,
                "email": email,
                "password": password,
            })

def valid_username_format(form):
    
    return form.is_valid()