from django.db import models 
from .abstract import Abstract
from .post import Post 
from .coment import Coment



class Like(Abstract):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    coment = models.ForeignKey(Coment, on_delete=models.CASCADE, null=True, blank=True)
    
