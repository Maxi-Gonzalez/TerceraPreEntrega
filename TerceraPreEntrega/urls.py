from django.urls import path
from TerceraPreEntrega import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('cafes/',views.cafes,name="cafes"),
    path('products/',views.products,name="products"),
    path('about/',views.about,name="about"), 
    path('cafe-Form/', views.cafe_Form,name="CafeForm"),
    path('cafe-Form2/', views.cafe_form2,name="CafeForm2"),
    path('buscar/', views.buscar, name="Buscar")
]

urlpatterns +=[
    path('vista/',views.CafeListView.as_view() ,name="Inicio"),
    path('vista/create/',views.CafeCreateView.as_view(),name="Create"), 
    path('vista/cafe-Form/', views.cafe_Form,name="CafeForm"),
    path('vista/cafe-Form2/', views.cafe_form2,name="CafeForm2"),
    path('vista/buscar/', views.buscar, name="Buscar")
]