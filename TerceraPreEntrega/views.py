from django.shortcuts import render
from TerceraPreEntrega.models import Cafe
from TerceraPreEntrega.forms import CafeFormulario, Buscar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



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
        
        cafe =  Cafe(nombre=request.POST['nombre'],precio=request.POST['precio'])

        cafe.save()

        return render(request, "TerceraPreEntrega/index.html")
    
    return render(request, "TerceraPreEntrega/cafeFormulario.html")


def cafe_form2(request):
 
    if request.method == "POST":
 
        miFormulario = CafeFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Cafe(nombre=informacion["nombre"], camada=informacion["precio"])
            curso.save()
        return render(request, "TerceraPreEntrega/index.html")
    else:
            miFormulario = CafeFormulario()
 
    return render(request, "TerceraPreEntrega/cafeFormulario2.html", {"formulario": miFormulario})

def buscar(request):
    if request.method == "POST":
        miFormulario = Buscar(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            cafe =Cafe.objects.filter(nombre__icontains=info["nombre"])
            return render(request,"TerceraPreEntrega/buscar.html",{"cafes":cafe} )
    else:
        miFormulario = Buscar()
 
    return render(request, "TerceraPreEntrega/buscar.html", {"formulario": miFormulario})

class CafeListView(ListView):
    model = Cafe
    template_name="TerceraPreEntrega/clase_list.html"

class CafeCreateView(CreateView):
    model= Cafe
    success_url="/TerceraPreEntrega/"
    fields = ["nombre","precio"]
