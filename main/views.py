from django.shortcuts import render, get_object_or_404
from main.models import Vinyl, Artist

def home(request):
    artists = Artist.objects.all()
    vinyls = Vinyl.objects.all()
    context = {
        'artists': artists,
        'vinyls': vinyls,
    }
    return render(request, 'home.html', context=context)

def about(request):
    return render(request, 'about.html', {'title': 'about us'})

def vinyl_detail(request, pk):
    vinyl = get_object_or_404(Vinyl, pk=pk)
    context = {
        'vinyl': vinyl,
        'title': vinyl.title,
    }
    return render(request, 'vinyl_detail.html', context=context)

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    vinyls = artist.vinyls.all()
    artists = Artist.objects.all()
    return render(request, 'artist_detail.html', {
        'artist': artist,
        'vinyls': vinyls,
        'artists': artists,
    })
