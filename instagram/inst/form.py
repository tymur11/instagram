from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .models import User 


class Register(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class Login(AuthenticationForm):
    class Meta:
        model = User 
        fields = ['username', 'password']