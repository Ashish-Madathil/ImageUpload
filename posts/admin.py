from django.contrib import admin
from .models import Post    # importing (class Post) from models.py file '.models' because models.py is at same level and directory as admins.py 
# Register your models here.
admin.site.register(Post)    # pass in the model(Post)