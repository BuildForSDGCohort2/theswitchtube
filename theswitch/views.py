from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoPost, VideoCategory, AudioPost, AudioCategory, VideoComment, AudioComment
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from .forms import VideoCategoryForm, AudioCategoryForm, VideoForm, AudioForm, VideoCommentForm, AudioCommentForm
from django.contrib.auth.decorators import login_required
from users.models import ProfilePic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


# Create your views here.
def homepage(request):
    return render(request, 'theswitch/homepage.html')


def home(request):
    audio = AudioPost.objects.order_by('upload')[:8]
    video = VideoPost.objects.order_by('upload')[:5]
    musics = AudioPost.objects.order_by('upload')[:6]

    context = {'audio': audio, 'video': video,
               'musics': musics}

    return render(request, 'theswitch/index.html', context)


def singlevideo(request, video_id):
    """Getting the id of each post and displaying content"""
    video = VideoPost.objects.get(id=video_id)
    # Getting The first five post from site
    video_5 = VideoPost.objects.order_by('?')[:4]

    if request.method != 'POST':
        # No data Submitted, Return blank form
        form = VideoCommentForm()

    else:
        # Post Data Submitted, process Data
        # setting default values for the form
        form = VideoCommentForm(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.name = request.user
            new_data.comment = video
            form.save()
            return HttpResponseRedirect(reverse('theswitch:singelevid', args=[int(video_id)]))

    # Disable and enable Comment of users that has comment
    comment_stuff = get_object_or_404(VideoPost, id=video_id)
    comment = True
    if comment_stuff.comments.filter(name=request.user).exists():
        comment = False

    # Get Likes and Count
    stuff = get_object_or_404(VideoPost, id=video_id)
    total_likes = stuff.total_likes()
    liked = True
    if stuff.likes.filter(id=request.user.id).exists():
        liked = False

    context = {'video': video, 'video5': video_5, 'videos': videos, 'total_likes': total_likes,
               'liked': liked, 'form': form, 'comment': comment}
    return render(request, 'theswitch/video-single.html', context)


def singleaudio(request, audio_id):
    """Getting the id of each post and displaying content"""
    audio = AudioPost.objects.get(id=audio_id)
    # Getting The first five post from site
    audios = AudioPost.objects.order_by('?')[:4]

    if request.method != 'POST':
        # No data Submitted, Return blank form
        form = AudioCommentForm()

    else:
        # Post Data Submitted, process Data
        # setting default values for the form
        form = AudioCommentForm(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.name = request.user
            new_data.comment = audio
            form.save()
            return HttpResponseRedirect(reverse('theswitch:singleaudio', args=[int(audio_id)]))

    # Disable and enable Comment of users that has comment
    comment_stuff = get_object_or_404(AudioPost, id=audio_id)
    comment = True
    if comment_stuff.comments.filter(name=request.user).exists():
        comment = False

    # Get Likes and Count
    stuff = get_object_or_404(AudioPost, id=audio_id)
    total_likes = stuff.total_likes()
    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True

    context = {'total_likes': total_likes, 'liked': liked, 'audio': audio, 'audios': audios, 'form': form,
               'comment': comment}
    return render(request, 'theswitch/audio-single.html', context)


def music(request):
    """Getting all Audios and Displaying Their Content"""

    musics = AudioPost.objects.all().order_by('-date')

    # numbers of post by page
    pages = Paginator(musics, 4)

    # Get the page number
    page_number = request.GET.get('page')
    page = pages.get_page(page_number)

    context = {'musics': musics, 'page': page}
    return render(request, 'theswitch/music.html', context)


def videos(request):
    """Getting all video post"""
    videos = VideoPost.objects.order_by('-date')
    # numbers of post by page
    pages = Paginator(videos, 4)

    # Get the page number
    page_number = request.GET.get('page')
    page = pages.get_page(page_number)

    context = {'videos': videos, 'page': page}
    return render(request, 'theswitch/videos.html', context)


@login_required()
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


@login_required()
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


@login_required()
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
            new_data = form.save(commit=False)
            new_data.user = request.user
            form.save()
            return redirect('theswitch:home')
    context = {'form': form}
    return render(request, 'theswitch/NewVideo.html', context)


@login_required()
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
            new_data = form.save(commit=False)
            new_data.user = request.user
            form.save()
            return redirect('theswitch:home')
    context = {'form': form}
    return render(request, 'theswitch/NewAudio.html', context)


@login_required()
def audiopost_edith(request, audio_id):
    """Edit An Existing Post"""
    audio = AudioPost.objects.get(id=audio_id)
    post = audio.category

    if audio.user != request.user:
        raise Http404

    if request.method != 'POST':
        # Pre-filled form with Existing content
        form = AudioForm(instance=audio)

    else:
        # Post Data Submitted and process
        form = AudioForm(request.POST, request.FILES, instance=audio)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.user = request.user
            form.save()

        return redirect('theswitch:musicpage')
    context = {'form': form, 'audio': audio, 'post': post}
    return render(request, 'theswitch/audioedit.html', context)


@login_required()
def videopost_edith(request, video_id):
    """Edit An Existing Post"""
    video = VideoPost.objects.get(id=video_id)
    post = video.category

    if video.user != request.user:
        raise Http404

    if request.method != 'POST':
        # Pre-filled form with Existing content
        form = VideoForm(instance=video)

    else:
        # Post Data Submitted and process
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.user = request.user
            form.save()

        return redirect('theswitch:videos')
    context = {'form': form, 'video': video, 'post': post}
    return render(request, 'theswitch/videoedit.html', context)


@login_required()
def audiopostcat_edith(request, audiocat_id):
    """Edit An Existing Post"""
    audio = AudioCategory.objects.get(id=audiocat_id)
    post = audio.name

    if audio.user != request.user:
        raise Http404

    if request.method != 'POST':
        # Pre-filled form with Existing content
        form = AudioCategoryForm(instance=audio)

    else:
        # Post Data Submitted and process
        form = AudioCategoryForm(instance=audio, data=request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.user = request.user
            form.save()

        return redirect('theswitch:home')
    context = {'form': form, 'audio': audio, 'post': post}
    return render(request, 'theswitch/audiocatedit.html', context)


@login_required()
def videopostcat_edith(request, videocat_id):
    """Edit An Existing Post"""
    video = VideoCategory.objects.get(id=videocat_id)
    post = video.name

    if video.user != request.user:
        raise Http404

    if request.method != 'POST':
        # Pre-filled form with Existing content
        form = VideoCategoryForm(instance=video)

    else:
        # Post Data Submitted and process
        form = VideoCategoryForm(instance=video, data=request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.user = request.user
            form.save()

        return redirect('theswitch:home')
    context = {'form': form, 'video': video, 'post': post}
    return render(request, 'theswitch/audiocatedit.html', context)


@login_required()
def profile_page(request):
    video = VideoPost.objects.filter(user=request.user).order_by('date')
    audio = AudioPost.objects.filter(user=request.user).order_by('date')
    pic = ProfilePic.objects.order_by('-date')
    context = {'audio': audio, 'video': video, 'user': request.user, 'pic': pic}
    return render(request, 'theswitch/profile.html', context)


# Video Likes
def likes(request, pk):
    post = get_object_or_404(VideoPost, id=request.POST.get('video_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('theswitch:singelevid', args=[str(pk)]))


# Audio likes
def likes2(request, pk):
    post = get_object_or_404(AudioPost, id=request.POST.get('audio_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('theswitch:singleaudio', args=[str(pk)]))




