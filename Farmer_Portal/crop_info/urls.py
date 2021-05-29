from django.urls import path,include
from . import views

urlpatterns = [
    path('product_info', views.crop_info, name = "Product Info page"),
    
]