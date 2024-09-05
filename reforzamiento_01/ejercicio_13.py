#13. Crear una lista vacía con 10 posiciones, pedir valores y devolver la suma y la media.

# Crear una lista vacía con 10 posiciones
lista_numeros = [0] * 10

# Pedir valores al usuario
for i in range(10):
    lista_numeros[i] = float(input(f"Ingrese el valor para la posición {i + 1}: "))

# Calcular la suma y la media
suma = sum(lista_numeros)
media = suma / len(lista_numeros)

# Mostrar la suma y la media
print("Suma de los números:", suma)
print("Media de los números:", media)

