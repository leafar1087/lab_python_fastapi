#12. Crear una lista con los 15 primeros números impares, agregar 3 números flotantes, y modificar la lista.

# Crear la lista con los 15 primeros números impares
numeros_impares = list(range(1, 30, 2))
print(numeros_impares)
# Agregar 3 números flotantes impares
numeros_impares.extend([3.1, 5.5, 7.7])
print(numeros_impares)
# Agregar una cadena en la posición 3
numeros_impares.insert(3, "Cadena")
print(numeros_impares)
# Eliminar la cadena de la lista
del numeros_impares[3]

# Mostrar la lista final
print("Lista final después de modificaciones:", numeros_impares)

