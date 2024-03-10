from django.db import models 
from .abstract import Abstract
from . import User 


class Chat(Abstract):
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='secondUser')
    
class Mesege(Abstract):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()