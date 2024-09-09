from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


from .models import Producto
from .forms import ProductoForm

def index(request):
    return render(request, 'producto/index.html')



#nueva version
def producto_list(request):
    query = request.GET.get('q')
    if query:
        producto = Producto.objects.filter(nombre_producto__icontains=query)
    else :
        producto = Producto.objects.all()
    contexto ={ 'producto':producto}
    return render(request, 'producto/producto_list.html',contexto)


def producto_detalle(request, pk:int):
    query = Producto.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'producto/producto_detalle.html', context)



def producto_beneficio(request, pk:int):
    query = Producto.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'producto/producto_beneficio.html', context)







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