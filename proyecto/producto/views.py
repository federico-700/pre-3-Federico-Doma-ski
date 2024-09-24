# Create your views here.
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




#***** INDEX FRUTA

def index(request):
    return render(request, 'producto/index.html')



#***** LIST FRUTA
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



#***** INDEX VERDURAS

def index_verduras(request):
    # Lógica para mostrar la vista de verduras
    #return render(request, 'verduras/index.html')

    return render(request, 'producto/index_verduras.html')



#***** LIST VERDURAS
def producto_list_verduras(request):
    query = request.GET.get('q')
    if query:
        producto = Producto.objects.filter(nombre_producto__icontains=query)
    else :
        producto = Producto.objects.all()
    contexto ={ 'producto':producto}
    return render(request, 'producto/producto_list_verduras.html',contexto)





















#***** CREATE VERDURAS
def producto_create_verduras(request):
    if request.method == 'GET':
        form= ProductoForm()
    
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("producto:producto_list_verduras")
    
    return render(request, 'producto/producto_create_verduras.html',{"form":form})



#***** DETAIL VERDURAS(DETALLES)
class ProductoDetailVerduras(DetailView):
    model = Producto
    template_name = 'producto/producto_detalle_verduras.html'




# ***** UPDATE VERDURAS

def producto_update_verduras(request,pk:int):
    query = Producto.objects.get(id=pk)
    if request.method == 'GET':
        form= ProductoForm(instance=query)
    
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:producto_list_verduras")
    
    return render(request, 'producto/producto_create_verduras.html',{"form":form})



#***** PRODUCTO BENEFICIO  VERDURAS


class ProductoBeneficioVerduras(DetailView):
    model = Producto
    template_name = 'producto/producto_beneficio_verduras.html'






#***** PRODUCTO DELETE VERDURAS

class ProductoDeleteVerduras(DeleteView):
    model = Producto
    template_name = 'producto/producto_confirm_delete_verduras.html'

   # success_url = reverse_lazy('producto:producto_list_verduras')