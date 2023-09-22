# Solución 
# Define una variable de cada tipo de primitivo:

var_int = 50
var_float = 50.3
var_string = "hola mundo"
var_boolean = False

# Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable

resultado = var_string + " INT: " + str(var_int) + " FLOAT: " + str(var_float) + " BOOLEAN: " + str(var_boolean)
print(resultado)

# Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo

"""
Los enteros en Python no tienen un límite fijo. El límite es la memoria disponible.
Para conocer el límite en tu sistema, puedes utilizar sys.maxsize o sys.maxint.
"""
import sys
print(f"Limite de los enteros en Python: {sys.maxsize}")

"""
Los flotantes en Python siguen el estándar IEEE 754 y tienen límites definidos.
El límite superior es aproximadamente 1.8 x 10^308, y el límite inferior es aproximadamente -1.8 x 10^308.
Los números que se acercan a estos límites se consideran "inf" (infinito).
"""
print(f"Límite superior de flotantes en Python: {float('1.79e308')}")
print(f"Límite inferior de flotantes en Python: {float('-1.79e308')}")

# Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable

"""
La fórmula es la siguiente:
S = n(n+1)
"""
# aplicandola para n = 80
n = 80
sum_pares = n * (n + 1)
print(f"La suma es: {sum_pares}")


