# contains information that'll enable the users to upload images
from django import forms
from .models import Post

class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title', 'image']