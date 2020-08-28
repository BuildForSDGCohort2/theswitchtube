"""Define Urls Pattern For Users"""

from django.urls import path, include
from . import views


app_name = 'theswitch'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home', views.home, name='home'),
    path('video/<int:video_id>', views.singlevideo, name='singelevid'),
    path('musics', views.music, name='musicpage'),
]
