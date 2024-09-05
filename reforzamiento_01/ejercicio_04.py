"""4. Contar cuántas veces se repite un curso, agregarlo a la lista, y eliminar el primer ítem por índice."""

cursos = ['Matemáticas', 'Física', 'Biología', 'Literatura', 'Informática', 'Economía', 'Derecho', 'Sociología']

# Agregar un curso repetido
cursos.append("Informática")

# Contar cuántas veces se repite "Informática"
repeticiones = cursos.count("Informática")

# Eliminar el primer ítem de la lista
del cursos[0]

# Mostrar la cantidad de repeticiones y la lista actualizada
print("Repeticiones de 'Informática':", repeticiones)
print("Lista después de eliminar el primer ítem:", cursos)

