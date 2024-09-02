from django.shortcuts import render , redirect
from .models import Frutas
from .forms import FrutasForm







def index(request):
    return render(request, 'frutas/index.html')



def frutas_list(request):
    query = request.GET.get('q')
    if query:
        frutas = Frutas.objects.filter(nombre_frutas__icontains=query)
    else :
        frutas =Frutas.objects.all()
    contexto ={ 'frutas':frutas}




    return render(request, 'frutas/frutas_list.html',contexto)




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



