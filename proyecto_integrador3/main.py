# Proyecto integrador parte 3

"""
Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:

Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os
"""


import os
import readchar as rch

def limpiar():
    """
        Esta funcion maneja el evento cls de la libreria os.
    """
    return os.system('cls' if os.name == 'nt' else 'clear')


def clear_write():
    
    """
        Esta funcion aumenta el valor de 'n' y borra la pantalla del terminal cuando se presiona la tecla 'N'
        del teclado.
    """
    n = 0
    print(f"\nPresione la tecla N para aumentar el valor de la variable 'n'")
    print(f"valor inicial de n: {n}")

    while n < 50:
        tecla =  rch.readkey()
        limpiar()
        if n < 50 and tecla == "n":
            n += 1 # es igual a decir que n = n + 1 // n = n - 1 <==> n -= 1 
            print(f"Valor actual de n: {n}")
        else:
            print(f"Recuerde que debe presionar la tecla N.")

    return "¡Tarea terminada! \nVuelva pronto :D"

print(clear_write())