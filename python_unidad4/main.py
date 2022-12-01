from camioneta import Camioneta
from coche import Coche
from bicicleta import Bicicleta
from motocicleta import Motocicleta
from vehiculo import Vehiculo
def main ():
    # Bloque principal
    # v1 = Vehiculo("rojo", 6)
    
    b1 = Bicicleta("verde", 2, "deportiva")
    mo1 = Motocicleta("azul", 2, "urbana",90, 100)
    co1 = Coche("negro", 4, 120, 50)
    ca1 = Camioneta("plateada", 4, 150, 80, 200)
    # lista_vehiculos = []
    # lista_vehiculos.append(type(b1).__name__)
    # lista_vehiculos.append(type(mo1).__name__)
    # lista_vehiculos.append(type(co1).__name__)
    # lista_vehiculos.append(type(ca1).__name__)
    # print(type(mo1).__name__) # recupera e imprime el nombre de una clase de un objeto
    # print(getattr(ca1, "color")) # devuelve el valor del atributo de la instancia de la clase
    # def catalogar (lista_vehiculos):
    #     i = 0
    #     for i  in range(len(lista_vehiculos)):
    #        print(lista_vehiculos[i])
           
    # catalogar(lista_vehiculos)
    vehiculos = []
    vehiculos.append(b1)
    vehiculos.append(mo1)
    vehiculos.append(co1)
    vehiculos.append(ca1)
    def catalogar(vehiculos = [], r = -1):
        count = 0
        v = []
        for Vehiculo in vehiculos:
            if Vehiculo.ruedas == r:
                # v = v + str(Vehiculo) + "\n"
                v.append("Tipo: " + str(type(Vehiculo).__name__))
                v.append("Características:  " + str(Vehiculo))
                count = count +vehiculos.count(Vehiculo)
        return f"Se han encontrado {count} vehículos con {r} ruedas.\nEstos son:{v}"
        # print(count)
        # print(v)
    print(catalogar(vehiculos, 2))
    
    # el contador funciona
    # count = 0
    # for i in range (len(vehiculos)):
    #     if str(vehiculos[i].ruedas) == "4":
    #         count = count + 1
    #     print(count)

if __name__ == "__main__":
    main()