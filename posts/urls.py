from django.urls import path

from .views import HomePageView, CreatePostView # HomePageView to display all the images uploaded on Home Page
# CreatePostView to upload new images
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post', CreatePostView.as_view(), name = 'add_post'),

]