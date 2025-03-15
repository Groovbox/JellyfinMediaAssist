from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Track
from django.urls import reverse


# Create your views here.
def index(request):

    tracks = Track.objects.all()

    return render(request, "mediaqueue/index.html", context={'tracks':tracks})

def new(request):
    return render(request, "mediaqueue/new.html")

def addsong(request):
    data = request.POST
    print(data)

    if data['track_title'] is not None:
        new_ = Track.objects.create(
            title = data['track_title'],
            alias = data['track_alias'],
            artists = data['track_artists'],
            album = data['track_album'],
            external_links = ",".join([data['track_ext_ytm'], data['track_ext_spt']]),
            genre = data['track_genres'],
            date = data['track_date']
        )
    return HttpResponseRedirect("/queue")

def lookup(request, source):
    pass