from django.db import models
from django.contrib.auth.models import User
from users.models import ProfilePic
from django.core.validators import FileExtensionValidator


# Create your models here.
class AudioCategory(models.Model):
    """Audio category model"""
    name = models.CharField("MediaCategories", unique=True, max_length=30)

    def __str__(self):
        """Return the sting representation of the model"""
        return self.name


class VideoCategory(models.Model):
    """Video category model"""
    name = models.CharField("MediaSecondCategories", unique=True, max_length=30)

    def __str__(self):
        """Return the sting representation of the model"""
        return self.name


class VideoPost(models.Model):
    """Post"""
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    date = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='media/video')
    cover = models.FileField(upload_to='media/videopic', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="video_post", blank=True)

    # Count Likes
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        """Return the sting representation of the model"""
        return self.header


class AudioPost(models.Model):
    """Post"""
    category = models.ForeignKey(AudioCategory, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    date = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='media/audio')
    cover = models.FileField(upload_to='media/audiopic', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="audio_post", blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        """Return the sting representation of the model"""
        return self.header


class VideoComment(models.Model):
    """Comment"""
    comment = models.ForeignKey(VideoPost, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.comment.title, self.name)


class AudioComment(models.Model):
    """Comment"""
    comment = models.ForeignKey(AudioPost, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.comment.title, self.name)

