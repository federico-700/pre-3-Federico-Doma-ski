from django.shortcuts import render , redirect
from .models import Frutas
from .forms import FrutasForm







def index(request):
    return render(request, 'frutas/index.html')

#version original , funciona
#def frutas_list(request):
#    frutas=Frutas.objects.all()
#    contexto ={ 'frutas':frutas}
#    return render(request, 'frutas/frutas_list.html',contexto)


def frutas_list(request):
    query = request.GET.get('q')
    if query:
        frutas = Frutas.objects.filter(nombre_frutas__icontains=query)
    else :
        frutas =Frutas.objects.all()
    contexto ={ 'frutas':frutas}




    return render(request, 'frutas/frutas_list.html',contexto)







#ejemplo
#def ofertas_list(request):
#    query = request.GET.get('q')
##    if query:
#        ofertas = Ofertas.objects.filter(nombre_ofertas__icontains=query)
#    else :
#        ofertas=Ofertas.objects.all()
#    contexto ={ 'ofertas':ofertas}
#    return render(request, 'ofertas/ofertas_list.html',contexto)


def frutas_create(request):
    if request.method == 'GET':
        form= FrutasForm()
    
    if request.method == "POST":
        form = FrutasForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("frutas:frutas_list")
    
    return render(request, 'frutas/frutas_create.html',{"form":form})










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
