from django.db import models
from . import User
class Abstract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modefait = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        

    
