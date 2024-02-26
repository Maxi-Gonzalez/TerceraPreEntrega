from django.http import HttpResponse

# Create your views here.
def inicio (request):
    return HttpResponse("Vista inicio")

def cafes(request):
    return HttpResponse("Vista cafes")

def products(request):
    return HttpResponse("Vista products")

def about(request):
    return HttpResponse("Vista about")