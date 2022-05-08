from django.http import HttpResponse
from django.shortcuts import render


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