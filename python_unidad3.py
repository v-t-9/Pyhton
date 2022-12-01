# 1) 
# class persona:
#     @property
#     def get_nombre(self):
#         return self._nombre
    
#     @property
#     def get_edad(self):
#         return self._edad

#     @get_nombre.setter
#     def set_nombre(self, nombre):
#         self._nombre= nombre
    
#     @get_edad.setter
#     def set_edad(self, edad):
#         self._edad= edad

# persona1 = persona()
# persona1.set_nombre = "Juan"
# persona1.set_edad = 22
# print("Mi nombre es: " , persona1.get_nombre)        #Para imprimir nombre desde afuera de la clase
# print("Mi edad es: " , persona1.get_edad)            #Para imprimir nombre desde afuera de la clase

# persona2 = persona()
# persona2.set_nombre = "María"
# persona2.set_edad = 15
# print("Mi nombre es: " , persona2.get_nombre)           #Para imprimir nombre desde afuera de la clase
# print("Mi edad es: " , persona2.get_edad)               #Para imprimir nombre desde afuera de la clase

# 2) 
# class persona:

#     def __init__(self, nom, ed):     
#          self._nombre = nom
#          self._edad = ed
#          print("Mi nombre es: " , self._nombre)
#          print("Mi edad es: " , self._edad)
    
#     @property
#     def get_nombre(self):
#         return self._nombre
    
#     @property
#     def get_edad(self):
#         return self._edad

#     @get_nombre.setter
#     def set_nombre(self, nombre):
#         self._nombre: nombre
    
#     @get_edad.setter
#     def set_edad(self, edad):
#         self._edad: edad

# persona1 = persona("Juan", 30)
# persona2 = persona("Maria", 25)

# 3)
# class persona:

#     def __init__(self, nom, ed):      
#          self._nombre = nom
#          self._edad = ed
#          print("Mi nombre es: " , self._nombre)
#          print("Mi edad es: " , self._edad)
    
#     @property
#     def get_nombre(self):
#         return self._nombre
    
#     @property
#     def get_edad(self):
#         return self._edad

#     @get_nombre.setter
#     def set_nombre(self, nombre):
#         self._nombre: nombre
    
#     @get_edad.setter
#     def set_edad(self, edad):
#         self._edad: edad

#     def es_mayor_de_edad(self):
#         if self._edad >= 18:
#             return print(True)
#         else:
#             return print(False)
        
##Bloque principal#
# persona1 = persona("Juan", 21)
# persona1.es_mayor_de_edad()
# #Para imprimir desde afuera de la clase:
# # print("Mi nombre es: " , persona1.get_nombre)
# # print("Mi edad es: " , persona1.get_edad)
# persona2 = persona("Maria", 15)
# persona2.es_mayor_de_edad()

# 4) 

# class persona:

#     def __init__(self, nombre, edad):  
#          self.nombre = nombre
#          self.edad = edad
#     def es_mayor_que(self,l = []):
#         for i in range(len(l)):
#             if l[i+1].edad > l[i].edad:
#                 return print(l[i+1].nombre, " es mayor que ", l[i].nombre) 
#             else:
#                 return print(l[i+1].nombre, " no es mayor que ", l[i].nombre) 

# #Bloque principal#
# persona1 = persona("Juana", 20)
# persona2 = persona("Pedro", 40)
# lista = []
# lista.append(persona1)
# lista.append(persona2)
# persona2.es_mayor_que(lista)

# 5)
# class persona:

#     def __init__(self,nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
        
#     @staticmethod
#     def get_mayor(l = []):
#         mayor = 0
#         nombre = " "
#         if l[0].edad > l[1].edad:
#             mayor = l[0].edad
#             nombre = l[0].nombre
#         else:
#             mayor =l[1].edad
#             nombre = l[1].nombre
       
#         return print("La persona mayor es:" ,nombre, "y tiene " , mayor, "años")
 
# #Bloque principal#
# lista = []
# #Lista de objetos
# lista.append(persona("Juana", 35))
# lista.append(persona("Pedro", 40))
# persona.get_mayor(lista)
# #print(str(lista[0].edad)) # funciona!!!!!

# 6) 
# class Alumno:
  
#     def __init__(self):
        
#         self.nombre = input("Ingrese el nombre del alumno: ")
#         self.nota = int(input("Ingrese la nota del alumno: "))
    
#     def __str__(self):
#         return f"El alumno { self.nombre} tiene la nota { self.nota}."
    
#     def resultado(self):
#         if(self.nota >= 4):
#             return f"{self.nombre} se encuentra aprobado/a"
#         else:
#             return f"{self.nombre} no se encuentra aprobado/a"

# Alumno1 = Alumno()
# print(Alumno1)
# print(Alumno1.resultado())

# 7)
# class Triangulo:
#     def __init__(self):
#         self.lado = []
#         for i in range(0,3,1):
#             lado = int(input("Ingrese lado del triangulo: "))
#             self.lado.append(lado)
    
#     def mayor(self):
#         return f"El lado mayor del triangulo es de: {max(self.lado)}"
    
#     def tipo_triangulo(self):
#         if self.lado[0] != self.lado[1] and self.lado[0] != self.lado[2] and self.lado[1] != self.lado[2]:
#             return f"El triangulo es escaleno"
#         if self.lado[0] == self.lado[1] and self.lado[0] ==self.lado[2]:
#             return f"El triangulo es equilatero"
#         else:
#             return f"El triangulo es isosceles"
##Bloque Principal#
# triangulo1 = Triangulo()
# print(triangulo1.mayor())
# print(triangulo1.tipo_triangulo())

# 8)
# class Calculadora:

#     def __init__(self):
#         self.num1 = int(input("Ingrese un numero:"))
#         self.num2 = int(input("Ingrese otro numero: "))
#         self.suma()
#         self.resta()
#         self.multiplicacion()
#         self.division()
    
#     def suma(self):
#         suma = self.num1+self.num2
#         return print("El resultado de la suma es" , suma)
    
#     def resta(self):
#         resta = self.num1-self.num2
#         return print("El resultado de la resta es ", resta)

#     def multiplicacion(self):
#         mutiplicacion = self.num1*self.num2
#         return print("El resultado de la multiplicacion es " , mutiplicacion)

#     def division(self):
#         division = self.num1/self.num2
#         return print("El resultado de la division es" , division)

# #Bloque Principal#
# calc1 = Calculadora()
# print(calc1)

# 9) 
# class Agenda:
  
#     def __init__(self):
#         self.nombre = []
#         self.telefono = []
#         self.email = []
#     def menu(self):
#         opcion = int(input("Bienvenido a la agenda!!!\nSeleccione una de las siguientes opciones:\n1 Añadir contacto\n2 Listar contactos\n3 Buscar contacto\n4 Editar contacto\n5 Cerrar agenda.\n"))
#         if opcion == 1:
#             return self.anadirContacto()
#         if opcion == 2:
#             return self.listarContacto()
#         if opcion == 3:
#             self.buscarContacto()
#         if opcion == 4:
#             self.editarContacto()
#         if opcion == 5:
#             return self.cerrarAgenda()

#     def anadirContacto(self):
#         nom = input("Ingrese el nombre del contacto " ,)
#         self.nombre.append(nom)
#         tel = int(input("Ingrese el telfono del contacto " ,))
#         self.telefono.append(tel)
#         email = input("Ingrese el email del contacto ", )
#         self.email.append(email)
#         rta = input("Quiere añadir otro contacto? s/n",)
#         if rta == "n" or rta=="N":
#               return self.menu()
#         while rta != "n" or rta!= "N":
#              return self.anadirContacto()

#     def listarContacto(self):
#         for i in range (len(self.nombre)):
#             print ("Nombre: ", self.nombre[i] , "\tTelefono:" , self.telefono[i], "\tEmail:" , self.email[i])
#         rta = input("Para volver al menu persione s",)
#         if rta == "s" or rta=="S":
#               self.menu()
#     def buscarContacto(self):
#         contacto = input("Ingrese contacto a buscar: ",)
#         for i in range (len(self.nombre)):
#             if contacto == self.nombre[i]:
#                 pos = i
#         print("El contacto buscado" , self.nombre[pos] , "tiene el telefono" , self.telefono[pos] ," y el email" , self.email[pos], ".")
#         rta = input("Para volver al menu persione s",)
#         if rta == "s" or rta=="S":
#               self.menu()
#     def editarContacto(self):
#         contacto = input("Ingrese contacto a editar: ",)
#         for i in range (len(self.nombre)):
#             if contacto == self.nombre[i]:
#                 pos = i
#         rta = input("Quiere editar el nombre?")
#         if rta == "si":
#             self.nombre[pos] = input("Ingrese nuevo nombre" ,)
#         rta = input("Quiere editar el telefono?")
#         if rta == "si":
#             self.telefono[pos] = input("Ingrese nuevo telefono" ,)
#         rta = input("Quiere editar el email?")
#         if rta == "si":
#             self.email[pos] = input("Ingrese nuevo email ", )
#         print(self.nombre[pos], self.telefono[pos], self.email[pos])
#         rta = input("Para volver al menu persione s",)
#         if rta == "s" or rta=="S":
#               self.menu()
#     def cerrarAgenda(self):
#         print("Fin!!!")

# #Bloque principal
# agenda1 = Agenda()
# print(agenda1.menu())

# 10)
# class Cliente:
    
#     def __init__(self, nom):
#         self.nombre = nom
#         self.cantidad = 0
#     def depositar(self, cantidad):
#         self.cantidad = self.cantidad + cantidad
#     def extraer(self, cantidad):
#         self.cantidad = self.cantidad - cantidad
#     def mostrar_total(self):
#          print("{} tiene depositada la suma de {}".format(self.nombre,self.cantidad))

# class Banco:
#     def __init__(self):
#         self.cliente1 = Cliente("Maria")
#         self.cliente2 = Cliente("Lucas")
#         self.cliente3 = Cliente("Marcos")
#     def operar(self):
#         self.cliente1.depositar(2000)
#         self.cliente1.extraer(500)
#         self.cliente2.depositar(5000)
#         self.cliente2.extraer(1000)
#         self.cliente3.depositar(1000)
#         self.cliente3.extraer(100)
#     def deposito_total(self, total=0):
#         total = (self.cliente1.cantidad) + (self.cliente2.cantidad) + (self.cliente3.cantidad)
#         self.cliente1.mostrar_total()
#         self.cliente2.mostrar_total()
#         self.cliente3.mostrar_total()
#         print("El total de dinero en el banco es: {}".format(total))

# #Bloque Principal
# banco1 = Banco()
# banco1.operar()
# banco1.deposito_total()

