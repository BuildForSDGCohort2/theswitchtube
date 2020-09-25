from django.urls import path, include
from  . import  views

"""Define URL patterns for Users"""

app_name = 'users'

urlpatterns = [
    # add auth urls (default)
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('edithprofilepic/<int:profile_id>', views.edith_profile, name='editprofile'),
    path('register2', views.profilepic, name='register2')
]
