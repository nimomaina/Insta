from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from tinymce.models import HTMLField


# Create your models here.
def post_save_user_model(sender,instance,created,*args,**kwargs):
   if created:
       try:
           Profile.objects.create(user = instance)
       except:
           pass
post_save.connect(post_save_user_model,sender=settings.AUTH_USER_MODEL)

class Profile(models.Model):
    profile_image = models.ImageField( blank=True, default='default.jpg', upload_to='profile/')
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
    caption = models.TextField(blank=True)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
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

class Comment(models.Model):
    pic = models.ForeignKey(Picture,blank=True, on_delete=models.CASCADE,related_name='comment')
    comment_owner = models.ForeignKey(User, blank=True)
    comment= models.CharField(max_length=255)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(pic__pk=id)
        return comments

    def __str__(self):
        return str(self.comment)

class Like(models.Model):
    pic = models.ForeignKey(Picture)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title

class Followers(models.Model):
    user = models.CharField(max_length=20,default='')
    Follower = models.CharField(max_length=20,default='')