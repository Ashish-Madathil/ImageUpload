"""imageUploadApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   #include will enable us to reference the urls.py file in the project
from django.conf import settings
from django.conf.urls.static import static  # to handle static files(CSS and Javascript files)

urlpatterns = [
    path('admin/', admin.site.urls),    # directs us to the admin page when '/admin' is entered and reference urls.py file for the project
    path('', include('posts.urls')),    # reference urls.py file for the app and include in the project urls.py file too
]

if settings.DEBUG:     # if it is in debug mode we have to add the URL of the media, so that we can view the uploaded image.
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # if we don't do that we won't be able to view uploaded images locally