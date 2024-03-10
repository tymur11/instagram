from . import User
from django.db import models 
from .abstract import Abstract

class Subscribe(Abstract):
    subscribers = models.ManyToManyField(User, related_name='subscribers')
    subscribe = models.ManyToManyField(User, related_name='subscribe_users')
