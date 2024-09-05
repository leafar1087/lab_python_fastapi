class Carro:
    ruedas = 4

    """Constructor: valores que van a tener por defecto mi clase que se le instanciará a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        self.velocidad = self.velocidad - self.aceleracion
        if self.velocidad < 0:
            self.velocidad = 0

carro1 = Carro("Negro",50)


carro1.acelera()
carro1.acelera()
carro1.acelera()
carro1.acelera()

print(f"El carro es de color: {carro1.color} y su velocidad es de {carro1.velocidad}")

carro1.frena()

print(f"El carro es de color: {carro1.color} y su velocidad es de {carro1.velocidad}")