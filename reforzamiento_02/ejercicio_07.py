#7. Crear un diccionario con 6 departamentos, borrar uno y comprobar que no existe.

# Crear un diccionario con 6 departamentos
departamentos = {
    "Madrid": "Capital",
    "Barcelona": "Costa",
    "Sevilla": "Sur",
    "Valencia": "Este",
    "Bilbao": "Norte",
    "Zaragoza": "Centro"
}
print("Departamentos antes de eliminar Barcelona:", departamentos)

# Borrar un departamento
del departamentos["Barcelona"]

# Comprobar que el departamento ha sido eliminado
print("Departamentos después de eliminar Barcelona:", departamentos)
