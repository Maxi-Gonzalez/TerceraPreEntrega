from django.urls import path
from TerceraPreEntrega import views

urlpatterns = [
    path('',views.inicio),
    path('cafes',views.cafes),
    path('products',views.products),
    path('about',views.about), 
]