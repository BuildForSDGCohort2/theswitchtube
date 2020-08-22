"""Define Urls Pattern For Users"""

from django.urls import path, include
from . import views


app_name = 'theswitch'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:post_id>', views.singlepost, name='singlepost'),
    path('home', views.home, name='home')
]
