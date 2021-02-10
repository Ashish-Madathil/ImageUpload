#from django.shortcuts import render
from django.views.generic import ListView, CreateView # List images on the Home Page(ListView) and upload new images(CreateView)
from django.urls import reverse_lazy    # to handle the redirect back to our own page after we have submitted the form So the upload is going to be via a form.
# So once the user uploaded and submitted that to the form, we want to redirect them back to the home page to display the image and the reverse on the scroll.
from .forms import PostForm     # Since the users won't have access to the admin site, we want them to be able to upload an image via a form
from .models import Post
# Create your views here.

class HomePageView(ListView): # extends from the ListView to enable listing of all images on the home page
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # to enable users to upload new images
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
