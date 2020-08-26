from django.db import models


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
    upload = models.FileField(upload_to='media/%Y/%m/%d/')
    cover = models.FileField(upload_to='media', blank=True)

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
    upload = models.FileField(upload_to='media/%Y/%m/%d/')
    cover = models.FileField(upload_to='media', blank=True)

    def __str__(self):
        """Return the sting representation of the model"""
        return self.header

