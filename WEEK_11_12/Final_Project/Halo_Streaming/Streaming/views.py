from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Streamingdata


@login_required
def mainpage(request):
    movies = Streamingdata.objects.all()
    return render(request, 'streaming/mainpage.html', {'movies': movies})


def watch(request, id):
    video = Streamingdata.objects.get(id=id)
    return render(request, 'streaming/movies_watch.html', {'video': video})
