from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.Login, name='Login'),
    path('register', views.Register, name='Register'),
]
