from django.shortcuts import render
from TerceraPreEntrega.models import Cafe

# Create your views here.
def inicio(request):
    return render(request,"TerceraPreEntrega/index.html")

def cafes(request):
    cafes=Cafe.objects.all()  #Esto me trae todo de la base de datos sql

    return render(request,"TerceraPreEntrega/cafes.html",{"cafes":cafes})

def products(request):
    return render(request, "TerceraPreEntrega/products.html")

def about(request):
    return render(request, "TerceraPreEntrega/about.html")

def cafe_Form(request):

    if request.method == 'POST':
        
        curso =  Cafe(request.post['nombre'],(request.post['precio']))

        curso.save()

        return render(request, "TerceraPreEntrega/inicio.html")
    
    return render(request, "TerceraPreEntrega/cafeFormulario.html")
