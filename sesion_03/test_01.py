class Carro:
    ruedas = 4

    """Constructor: valores que van a tener por defecto mi clase que se le instanciará a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos"""
    def aceleracion(self):
        self.velocidad = self.velocidad + self.aceleracion()

    def frena(self):
        self.velocidad = self.velocidad - self.aceleracion()
        if self.velocidad < 0:
            self.velocidad = 0



"""Instanciamos nuestra clase"""
carro1= Carro('Negro',50)
print(f"El carro es de color: {carro1.color} y su aceleacion es de {carro1.aceleracion}")

carro2= Carro('Rojo',80)
print(f"El carro es de color: {carro2.color} y su aceleacion es de {carro2.aceleracion}")