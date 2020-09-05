"""Define Urls Pattern For Users"""

from django.urls import path, include
from . import views


app_name = 'theswitch'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home', views.home, name='home'),
    path('video/<int:video_id>', views.singlevideo, name='singelevid'),
    path('musics', views.music, name='musicpage'),
    path('videos', views.videos, name='videos'),
    path('vidcategory/', views.VidCategory, name='VidCategory'),
    path('audcategory/', views.AudCategory, name='AudCategory'),
    path('audiopost/', views.audiopost, name='audiopost'),
    path('videopost', views.videopost, name='videopost'),
    path('audiopost-edith<int:audio_id>', views.audiopost_edith, name='audiopost-edith'),
    path('videopost-edith<int:video_id>', views.videopost_edith, name='videopost-edith'),
    path('audiopostcat-edith<int:audiocat_id>', views.audiopostcat_edith, name='audiopostcat-edith'),
    path('videopostcat-edith<int:videocat_id>', views.videopostcat_edith, name='videopostcat-edith'),
]
