from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from tinymce.models import HTMLField


# Create your models here.

class Profile(models.Model):
    profile_image =models.ImageField( blank=True, default='default.jpg', upload_to='profile/')
    bio = models.CharField(max_length=255)
    user = models.OneToOneField(User,blank=True, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return str(self.user)




    def profile_save(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(owner=id)
        return profile

    @classmethod
    def get_profile_by_username(cls, owner):
        profiles = cls.objects.filter(owner__contains=owner)
        return profiles


class Picture(models.Model):
    image = models.ImageField(upload_to='uploads/', default='default.jpg')
    name = models.CharField(max_length=30)
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    profile_details = models.ForeignKey(Profile)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)


    def save_pic(self):
        self.save()

    def delete_pic(self):
        self.delete()


    @classmethod
    def get_image_by_id(id):
        pic = Picture.objects.get(id)
        return pic

