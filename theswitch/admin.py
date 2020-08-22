from django.contrib import admin
from .models import VideoCategory, VideoPost, AudioCategory, AudioPost

# Register your models here.
admin.site.register(VideoCategory)
admin.site.register(VideoPost)
admin.site.register(AudioCategory)
admin.site.register(AudioPost)
