from django.shortcuts import render, redirect
from .models import Verduras
from .forms import VerdurasForm

def index(request):
    return render(request, 'verduras/index.html')













#original, funciona
#def ofertas_list(request):
#    ofertas=Ofertas.objects.all()
#    contexto ={ 'ofertas':ofertas}
#    return render(request, 'ofertas/ofertas_list.html',contexto)




#nueva version
def verduras_list(request):
    query = request.GET.get('q')
    if query:
        verduras = Verduras.objects.filter(nombre_verduras__icontains=query)
    else :
        verduras=  Verduras.objects.all()
    contexto ={ 'verduras':verduras}
    return render(request, 'verduras/verduras_list.html',contexto)







def verduras_create(request):
    if request.method == 'GET':
        form= VerdurasForm()
    
    if request.method == "POST":
        form = VerdurasForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("verduras:verduras_list")
    
    return render(request, 'verduras/verduras_create.html',{"form":form})




#def ofertas_create(request):
#    if request.method == 'GET':
#        form= OfertasForm()
#    
#    if request.method == "POST":
#        form = OfertasForm(request.POST)
#        if form.is_valid():
#            print(form.cleaned_data)
#            form.save()
#            return redirect("ofertas:ofertas_list")
#    
#    return render(request, 'ofertas/ofertas_create.html',{"form":form})