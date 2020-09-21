from django import forms
from .models import AudioCategory, VideoCategory, VideoPost, AudioPost


class VideoCategoryForm(forms.ModelForm):
    class Meta:
        model = VideoCategory
        fields = ['name']
        labels = ['Category', '']


class AudioCategoryForm(forms.ModelForm):
    class Meta:
        model = AudioCategory
        fields = ['name']
        labels = ['Category', '']


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoPost
        fields = ['header', 'artist', 'title', 'upload', 'cover', 'category']
        labels = {'header': 'Enter Header:', 'artist': 'Enter Artist Name', 'title': 'Enter Title',
                  'upload': 'Choose mp4 file:', 'cover': 'Choose a jpg or Png:', 'category': 'Select Category'}


class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioPost
        fields = ['header', 'artist', 'title', 'upload', 'cover', 'category']
        labels = {'header': 'Enter Header:', 'artist': 'Enter Artist Name', 'title': 'Enter Title',
                  'upload': 'Choose mp3 file:', 'cover': 'Choose a jpg or Png:', 'category': 'Select Category'}