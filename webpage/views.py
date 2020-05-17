from django.shortcuts import render, HttpResponse, get_list_or_404
from datetime import datetime
from .models import Room
# Create your views here.


def welcome(request):
    rooms = Room.objects.all()
    return render(request, "webpage/welcome.html",
                  {"rooms": rooms})


def current_date(request):
    return HttpResponse(datetime.utcnow())
