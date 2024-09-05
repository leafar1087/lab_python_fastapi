"""2. Agregar 4 objetos nuevos a la lista, quitar 2 elementos por valor y mostrar la lista final."""
from reforzamiento_01.ejercicio_01 import cursos

#cursos = ["Matemáticas", "Historia", "Física", "Química", "Biología", "Literatura"]

# Agregar 4 objetos nuevos
cursos.append("Informática")
cursos.append("Economía")
cursos.append("Derecho")
cursos.append("Sociología")

# Quitar 2 elementos por valor
cursos.remove("Historia")
cursos.remove("Química")

# Mostrar la lista final
print("Lista final:", cursos)
