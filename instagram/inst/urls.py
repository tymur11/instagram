from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.Main.as_view()), name='main'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', login_required(views.LogoutPage.as_view()), name='Logout'),
    path('makepost/',login_required(views.MakePost.as_view()), name='makepost'),
    path('userpage/<int:id>/', login_required(views.UserPage.as_view()), name='userpage'),
    path('post/<int:id>/', login_required(views.PostPage.as_view()), name='postpage'),
    path('profilPage/', login_required(views.ProfilPage.as_view()), name='profilPage'),
    path('search/', login_required(views.SearchPage.as_view()), name='searchPage'),
    path('chat/<int:id>/',login_required(views.ChatPage.as_view()), name='Chat'),
    path('makechat/<int:id>/', login_required(views.ChatCreate.as_view()),name='ChatPage')
]
