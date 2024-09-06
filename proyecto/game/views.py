
from django.shortcuts import render , redirect
import random
import time


def index(request):
    # Generar un número aleatorio
    numero_aleatorio = random.randint(1, 10)
    premio = ""

    # Mostrar una cuenta regresiva de 3 segundos
    print("....sorteo....")
    for i in range(1, 0, -1):
        print(i)
        time.sleep(1)

    # Determinar el premio basado en el número aleatorio
    if numero_aleatorio == 1:
        premio = "Seguí participando"
    elif 2 <= numero_aleatorio <= 5:
        premio = "¡Premio! Ganaste un 30% de descuento en todas las frutas y verduras!"
    elif 6 <= numero_aleatorio <= 8:
        premio = "¡Premio! Ganaste un 50% de descuento en todas las frutas y verduras!"
    elif numero_aleatorio in [9, 10]:
        premio = "¡Premio! Una orden de compras de 100.000 pesos!"

    # Pasar el premio al template
    context = {'premio': premio}
    return render(request, 'game/index.html', context)





