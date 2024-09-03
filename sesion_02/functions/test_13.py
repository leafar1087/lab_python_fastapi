"""
Programación funcional en Python

Ejercicio en clase
"""

"""
Requisitos:
- Solicitar al usuario 4 números por consola
- Crear una función que devuelva cuál es el mayor número de los 4 ingresado por el usuario
- Finalmente elevar al cubo este resultado
"""

# Solicitar al usuario 4 números por consola
numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(4)]

# Función para devolver el mayor número de los 4 ingresados
def obtener_mayor_numero(numeros):
    return max(numeros)

# Obtener el mayor número
mayor_numero = obtener_mayor_numero(numeros)

# Elevar al cubo el mayor número
resultado_cubo = mayor_numero ** 3

print(f"El mayor número es: {mayor_numero}")
print(f"El mayor número elevado al cubo es: {resultado_cubo}")
