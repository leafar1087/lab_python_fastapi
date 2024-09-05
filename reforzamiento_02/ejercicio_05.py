#5. Convertir el diccionario a una lista y mostrar el tipo de datos final.

from reforzamiento_02.ejercicio_01 import persona

# Convertir el diccionario a una lista de tuplas (clave, valor)
diccionario_a_lista = list(persona.items())

# Mostrar el tipo de datos final
print("Tipo de datos final de la lista:", type(diccionario_a_lista))


