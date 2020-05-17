from django.shortcuts import render, get_object_or_404, get_list_or_404
from webpage.models import Meeting, Room
# Create your views here.


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html",
                  {"meeting": meeting})


def detail_room(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/detail_room.html",
                  {"room": room})
