from django.db import models 
from .abstract import Abstract
from .post import Post 



class Coment(Abstract):
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
