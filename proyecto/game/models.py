from django.db import models
import random
import time

"""Game 1, el usuario por usar la aplicacion tiene premios y descuentos / 
No esta terminado aun, la idea seria que por abrir la aplicacion, cada 24 hs tenga algun premio aleatorio.
La gamificacion en las aplicaciones es cada vez mas usual. Coderhouse implementa esto, sumas puntos, ganas descuentos etc.
 """

class Game(models.Model):
    # Generar un número aleatorio entre 1 y 10
    numero_aleatorio = random.randint(1, 10)

    # Mostrar una cuenta regresiva de 3 segundos
    print("....sorteo....")
    for i in range(1, 0, ):
        print(i)
        time.sleep(1)

    # Determinar el premio basado en el número aleatorio
    if numero_aleatorio == 1:

        print("Seguí participando")
    elif 2 <= numero_aleatorio <= 5:

        print("¡Premio! Ganaste un 30% de descuento en todas las frutas y verduras!")
    elif 6 <= numero_aleatorio <= 8:

        print("¡Premio! Ganaste un 50% de descuento en todas las frutas y verduras!")
    elif numero_aleatorio in [9, 10]:

        print("¡Premio! Una orden de compras de 100.000 pesos!")





