from django.contrib import admin
from .models import VideoCategory, VideoPost, AudioCategory, AudioPost, VideoComment, AudioComment

# Register your models here.
admin.site.register(VideoCategory)
admin.site.register(VideoPost)
admin.site.register(AudioCategory)
admin.site.register(AudioPost)
admin.site.register(VideoComment)
admin.site.register(AudioComment)


class MyAwesomeModelWithFiles(admin.ModelAdmin):
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'

