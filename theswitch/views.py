from django.shortcuts import render, redirect
from .models import VideoPost, VideoCategory, AudioPost, AudioCategory
import random
from .forms import VideoCategoryForm, AudioCategoryForm, VideoForm, AudioForm


# Create your views here.
def homepage(request):
    return render(request, 'theswitch/homepage.html')


def home(request):
    audio = AudioPost.objects.order_by('upload')[:5]
    video = VideoPost.objects.order_by('upload')[:5]
    musics = AudioPost.objects.order_by('upload')[:6]
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


def videos(request):
    """Getting all video post"""
    videos = VideoPost.objects.order_by('date')
    context = {'videos': videos}
    return render(request, 'theswitch/videos.html', context)


def VidCategory(request):
    """Add new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = VideoCategoryForm()

    else:

        # Post data submitted; process data
        form = VideoCategoryForm(data=request.POST)
        if form.is_valid():
            # new_category = form.save(commit=False)
            # new_category.owner = request.user
            # new_category.save()
            form.save()
            return redirect('theswitch:home')

    context = {'form': form}
    return render(request, 'theswitch/newVidCategory.html', context)


def AudCategory(request):
    """Add new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = AudioCategoryForm()

    else:

        # Post data submitted; process data
        form = AudioCategoryForm(data=request.POST)
        if form.is_valid():
            # new_category = form.save(commit=False)
            # new_category.owner = request.user
            # new_category.save()
            form.save()
            return redirect('theswitch:home')

    context = {'form': form}
    return render(request, 'theswitch/newAudCategory2.html', context)


def videopost(request):
    """Add a new post for a particular Video"""

    if request.method != 'POST':
        # No data Submitted, Return blank form
        form = VideoForm()

    else:
        # Post Data Submitted, process Data
        # setting default topic Value
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('theswitch:home')
    context = {'form': form}
    return render(request, 'NewVideo.html', context)


def audiopost(request):
    """Add a new post for a particular Audio"""

    if request.method != 'POST':
        # No data Submitted, Return blank form
        form = AudioForm()

    else:
        # Post Data Submitted, process Data
        # setting default topic Value
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('theswitch:home')
    context = {'form': form}
    return render(request, 'theswitch/NewAudio.html', context)

