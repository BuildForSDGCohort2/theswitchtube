from django.shortcuts import render
from .models import VideoPost, VideoCategory, AudioPost, AudioCategory


# Create your views here.
def homepage(request):
    """Getting all post"""
    media = VideoPost.objects.all()
    context = {'media': media}
    return render(request, 'theswitch/homepage.html', context)


def home(request):
    return render(request, 'theswitch/index.html')
