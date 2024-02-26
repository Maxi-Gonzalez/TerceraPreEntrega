from django.urls import path
from TerceraPreEntrega import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('cafes/',views.cafes,name="cafes"),
    path('products/',views.products,name="products"),
    path('about/',views.about,name="about"), 
    path('cafe-Form/', views.cafe_Form,name="CafeForm")
]