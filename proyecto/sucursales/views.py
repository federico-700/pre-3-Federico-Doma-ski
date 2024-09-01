from django.shortcuts import render,redirect
from .models import Sucursales
from .forms import SucursalesForm




def index(request):
    return render(request, 'sucursales/index.html')


def sucursales_list(request):
    query = request.GET.get('q')
    if query:
        sucursales = Sucursales.objects.filter(nombre_sucursales__icontains=query)
    else :
        sucursales =Sucursales.objects.all()
    contexto ={ 'sucursales':sucursales}

    return render(request, 'sucursales/sucursales_list.html',contexto)




#def frutas_list(request):
#    query = request.GET.get('q')
#    if query:
#        frutas = Frutas.objects.filter(nombre_frutas__icontains=query)
#    else :
#        frutas =Frutas.objects.all()
#    contexto ={ 'frutas':frutas}
#
#    return render(request, 'frutas/frutas_list.html',contexto)





def sucursales_create(request):
    if request.method == 'GET':
        form= SucursalesForm()
    
    if request.method == "POST":
        form = SucursalesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("sucursales:sucursales_list")
    
    return render(request, 'sucursales/sucursales_create.html',{"form":form})






#def frutas_create(request):
#    if request.method == 'GET':
#        form= FrutasForm()
#    
#    if request.method == "POST":
#        form = FrutasForm(request.POST)
#        if form.is_valid():
##            print(form.cleaned_data)
#           form.save()
#            return redirect("frutas:frutas_list")
#    
#    return render(request, 'frutas/frutas_create.html',{"form":form})


