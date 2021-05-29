from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name = "home page"),
    path('login', views.login, name = "login page"),
]