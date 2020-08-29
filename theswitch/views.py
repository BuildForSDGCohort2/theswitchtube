from django.shortcuts import render
from .models import VideoPost, VideoCategory, AudioPost, AudioCategory
import random


# Create your views here.
def homepage(request):
    return render(request, 'theswitch/homepage.html')


def home(request):
    audio = AudioPost.objects.order_by('upload')[:5]
    video = VideoPost.objects.order_by('upload')[:5]
    musics = AudioPost.objects.order_by('upload')[:5]
    audio_cat = AudioCategory.objects.order_by('name')[0]
    audios = AudioCategory.objects.order_by('name')[1:5]
    context = {'audio': audio, 'video': video, 'audios': audios, 'audio_cat': audio_cat, 'musics': musics}
    return render(request, 'theswitch/index.html', context)


def singlevideo(request, video_id):
    """Getting the id of each post and displaying content"""
    video = VideoPost.objects.get(id=video_id)
    # Geting The first five post from site
    video_5 = VideoPost.objects.order_by('upload')[:4]
    videos = VideoPost.objects.order_by('?').first()
    context = {'video': video, 'video5': video_5, 'videos': videos}
    return render(request, 'theswitch/video-single.html', context)


def music(request):
    """Getting all Audios and Displaying Their Content"""
    musics = AudioPost.objects.all()
    context = {'musics': musics}
    return render(request, 'theswitch/music.html', context)



