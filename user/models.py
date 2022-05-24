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
    profile_pic = models.ImageField(upload_to='media/profile_pics', blank=True)
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

    # method to count the number of farmers
    @staticmethod
    def count_farmers():
        return User.objects.filter(is_farmer=True).count()


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

