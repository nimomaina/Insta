from django import forms
from .models import *

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('image', 'caption')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['owner']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['imagey', 'comment_owner']