import readchar as rch

nombre_jugador = input("Ingresa tu nombre: ")
print(f"Bienvenido al juego {nombre_jugador}!! :D")

#Segunda parte del juego:

print(f".\n.\n.\nPresione una tecla!! :D")

while True:
    tecla = rch.readkey()
    print(f"Tecla presionada: {tecla}")
    if tecla == rch.key.UP:
        print(f"Ha presionado la tecla {tecla}, por lo tanto, el programa ha terminado.")
        break
