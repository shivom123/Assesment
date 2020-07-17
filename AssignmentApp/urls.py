from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
path('', views.Register, name='registration'),
path('login', views.loginView, name='login'),
path('profile', views.UserProfile, name='profile'),

]