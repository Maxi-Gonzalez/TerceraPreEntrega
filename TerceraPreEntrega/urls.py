from django.urls import path
from TerceraPreEntrega import views

urlpatterns = [
    path('',views.inicio),
    path('cursos',views.cursos),
]