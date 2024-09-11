# Create your views here.
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




#***** INDEX

def index(request):
    return render(request, 'producto/index.html')



#***** NUEVA VERSION

#***** LIST
def producto_list(request):
    query = request.GET.get('q')
    if query:
        producto = Producto.objects.filter(nombre_producto__icontains=query)
    else :
        producto = Producto.objects.all()
    contexto ={ 'producto':producto}
    return render(request, 'producto/producto_list.html',contexto)


# ***** UPDATE

def producto_update(request,pk:int):
    query = Producto.objects.get(id=pk)
    if request.method == 'GET':
        form= ProductoForm(instance=query)
    
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:producto_list")
    
    return render(request, 'producto/producto_create.html',{"form":form})




#***** CREATE
def producto_create(request):
    if request.method == 'GET':
        form= ProductoForm()
    
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("producto:producto_list")
    
    return render(request, 'producto/producto_create.html',{"form":form})




#***** PRODUCTO BENEFICIO  

class ProductoBeneficio(DetailView):
    model = Producto
    template_name = 'producto/producto_beneficio.html'


#***** PRODUCTO DELETE 

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto:producto_list')



#***** DETAIL (DETALLES)
class ProductoDetail(DetailView):
    model = Producto
    template_name = 'producto/producto_detalle.html'
