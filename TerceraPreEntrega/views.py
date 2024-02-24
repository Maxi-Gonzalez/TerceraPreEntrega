from django.shortcuts import render
from TerceraPreEntrega.models import Cafe

# Create your views here.
def inicio (request):
    return render(request,"index.html")

def cafes(request):
    cafes=Cafe.objects.all()  #Esto me trae todo de la base de datos sql
    
    return render(request,"TerceraPreEntrega/cafes.html",{"cafes":cafes})