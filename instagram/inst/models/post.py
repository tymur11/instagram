from django.db import models 
from .user import  User
from .abstract import Abstract


class Post(Abstract):
    text = models.CharField(max_length=100)
    imege = models.ImageField(upload_to='media/postimage')
    