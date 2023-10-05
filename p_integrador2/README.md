## Descripción del proyecto

Este programa es el inicio de un videojuego basado en texto, lo que hace es lo siguiente:

* pide un nombre al usuario:
    ```python
    nombre_jugador = input("Ingresa tu nombre: ")
    ```
* Imprime el nombre del jugador con un saludo de bienvenida:
    ```python
    print(f"Bienvenido al juego {nombre_jugador}!! :D")
    ```

Este es el primer paso para la creación del videojuego.

En el segundo paso para la creación del video se pidió instalar la libreria readchar. 

realicé lo siguiente:

* Importé la libreria readchar como rch.
* Luego con un ciclo while infinito, le pedí al usuario que presione una tecla. 
* Luego cuando el usuario presiona una tecla, se imprime en pantalla la tecla que el usuario ha presionado.
* Por último cuando el usuario presiona la tecla "UP" el programa se detiene.

    ```python
    import readchar as rch

    print(f".\n.\n.\nPresione una tecla!! :D")

    while True:
        tecla = rch.readkey()
        print(f"Tecla presionada: {tecla}")
        if tecla == rch.key.UP:
            print(f"Ha presionado la tecla {tecla}, por lo tanto, el programa ha terminado.")
            break
    ```
