from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + " tipo: {}".format(self.tipo)
