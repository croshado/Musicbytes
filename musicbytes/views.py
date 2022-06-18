
from django.shortcuts import render
from musicbytes.models import song 

from json import dumps

def index(request):
    songs = song.objects.all()
    return render(request, 'index.html', {'song':songs})

# Create your views here.
def songs(request):
    songs = song.objects.all()
    return render(request,'musicbytes/songs.html',{'song':songs})

def songpost(request,id):
    songs=song.objects.filter(song_id=id).first
    d=song.objects.last().song_id
   
    a=id+1
    
    if a>d:
        a=id
    
        
    b=id-1
    if b<3:
        
        b=id

        

    return render(request, 'songpost.html', {'song':songs, 'her':a, 'pre':b})

def search(request):
    query= request.GET.get("query")
    songs=song.objects.all()
    qs= songs.filter(name__icontains=query)
    return render(request, 'musicbytes/search.html',{'song':qs, 'query':query})
    




