from django.shortcuts import render
from musicbytes.models import song 
def index(request):
    songs = song.objects.all()
    return render(request, 'index.html', {'song':songs})