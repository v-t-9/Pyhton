from vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", velocidad: {} km/h, cilindrada: {} cc ".format(self.velocidad, self.cilindrada)