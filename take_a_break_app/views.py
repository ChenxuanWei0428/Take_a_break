from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



def start(request):
    return render(request, "take_a_break_app/start.html")

def still_building(request):
    return render(request, "take_a_break_app/still_building.html")