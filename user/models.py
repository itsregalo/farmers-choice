from django.db import models
from django.contrib.auth.models import AbstractUser

# Imagekit is a library for resizing an image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


class User(AbstractUser):
    # existing fields
    # username
    # first_name
    # last_name
    # email
    # password
    # is_active
    # is_superuser

    # new fields
    location = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    profile_file_thumbnail = ImageSpecField(source='profile_pic',
                                            processors=[ResizeToFill(494, 563)],
                                            format='JPEG',
                                            options={'quality': 60})
    is_farmer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # __str__ method to return username for the user
    def __str__(self):
        return self.username


