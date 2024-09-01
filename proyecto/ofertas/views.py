from django.shortcuts import render, redirect


from .models import Ofertas
from .forms import OfertasForm

def index(request):
    return render(request, 'ofertas/index.html')


#original, funciona
#def ofertas_list(request):
#    ofertas=Ofertas.objects.all()
#    contexto ={ 'ofertas':ofertas}
#    return render(request, 'ofertas/ofertas_list.html',contexto)




#nueva version
def ofertas_list(request):
    query = request.GET.get('q')
    if query:
        ofertas = Ofertas.objects.filter(nombre_ofertas__icontains=query)
    else :
        ofertas=Ofertas.objects.all()
    contexto ={ 'ofertas':ofertas}
    return render(request, 'ofertas/ofertas_list.html',contexto)








#def pais_list(request):
#    query = request.GET.get('q')
#    if query:
#        paises = Pais.objects.filter(nombre__icontains=query)
#    else :
#        paises = Pais.objects.all()
##    contexto = {'paises': paises}
#    return render(request, 'clientes/pais_list.html', contexto)





def ofertas_create(request):
    if request.method == 'GET':
        form= OfertasForm()
    
    if request.method == "POST":
        form = OfertasForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("ofertas:ofertas_list")
    
    return render(request, 'ofertas/ofertas_create.html',{"form":form})

