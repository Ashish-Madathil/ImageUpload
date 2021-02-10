from django.db import models

class Post(models.Model):           #class Post(to create database table) inherits from models. inside models, there is a class called Model
    title = models.CharField(max_length = 200) # CharField is adatatype expecting max 200 characters
    image = models.ImageField(upload_to = 'images/') # references models again, ImageField datatype referencing where to upload images to
# uploading to a directory called 'images' which is placed in a directory called 'media'
    def __str__(self):
        return self.title  # (only title is displayed in the admin page) to view the model inside the admin page of this project, it will return whatever title given to the uploaded images
# Create your models here.
