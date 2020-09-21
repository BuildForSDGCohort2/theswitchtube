from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProfilePic(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_image = models.FileField(verbose_name="Profile Picture", upload_to="media/profile/", blank=True, null=True)
    bio = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


