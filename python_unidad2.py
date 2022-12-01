import datetime
import math
#1) 
# def el_mayor_de_los_numeros(num1, num2, num3):
#   lista_numeros = [num1, num2, num3]
   
#   if num1 == num2:
#     if num1>=num3: #Implica que el mayor es repetido
#       return print(-1)
#     else: 
#       return print(max(lista_numeros))
#   if num1 == num3:
#     if num1>=num2:
#       return print(-1)
#     else: 
#       return print(max(lista_numeros))
#   if num2 == num3:
#     if num2>=num1:
#       return print(-1)
#     else:
#       return print(max(lista_numeros))

#   return  print(max(lista_numeros))

# el_mayor_de_los_numeros(5,2,2)

# 1.2)
# lista_numeros = []
# for num in range (0,3,1):
#   num = int(input("Inrgrese un numero: "))
#   lista_numeros.append(num)

# def el_mayor_de_los_numeros(lista):

#   if lista[0] == lista[1]:
#     if lista[0]>=lista[2]: #Implica que el mayor es repetido
#       return print("El mayor absoluto de:" , lista , "no existe.")
#     else: 
#       return print(max(lista))
#   if lista[0] == lista[2]:
#     if lista[0] >= lista[1]:
#       return print("El mayor absoluto de:" , lista , "no existe.")
#     else: 
#       return print(max(lista))
#   if lista[1] == lista[2]:
#       if lista[1] >= lista[0]:
#         return print("El mayor absoluto de:" , lista , "no existe.")
#       else:
#         return print(max(lista))

#   return  print(max(lista))

# el_mayor_de_los_numeros(lista_numeros)
  
# 2) 
# dia = int (input("Ingrese un día:" ,))
# mes = int (input("Ingrese un mes:" ,))
# año = int (input("Ingrese un año:" ,))

# def fecha_valida(d, m, a):
  
#     fecha = datetime.date(a, m, d)
#     hoy = datetime.date.today()

#     if fecha>=hoy:
#         print(True)
#     else:
#         print(False)
 
# fecha_valida(dia, mes, año)

#3) .
# total_compra = int(input("Ingrese el monto total de la compra: "))
# dinero_recibido = int(input("Ingrese el monto de dinero recibido: "))

# if total_compra > dinero_recibido:
#     print("El dinero recibido es insuficiente. ")
# if total_compra == dinero_recibido:
#     print("No hay vuelto.")

# if total_compra < dinero_recibido:
#     vuelto = dinero_recibido - total_compra

#     billetes = [500, 100, 50, 20, 10, 5,1]
#     dinero = []
#     cant= []
   
#     for i in billetes:
        
#         if vuelto/i > 0:
#             if vuelto >= i:
#                 cantidad = math.floor(vuelto/i)
#                 vuelto = vuelto%i
#                 cant.append(cantidad)
#                 dinero.append(i)

#     print("El vuelto es: ")
#     for i in range (len(cant)) and range (len(dinero)):
#         print(cant[i] , "billete/s de ", dinero[i] )

# 4) 

# cant_filas = int(input("Ingrese cantidad de filas: " ))
# def partones_asteriscos(filas):
#    for i in range(1, filas+1):
#       print("*" * 10)

#    print("\n")
# ###############################################
#    print("*")
#    for i in range(1, filas):
#       print(("*" * i * 2))

# partones_asteriscos(cant_filas)

# 5)
# n = int(input("Ingrese numero: " ))
# cuad = lambda num: num**2     #funcion lambda
# print(cuad(n))                #llamado a la funcion lambda

# 6) 
# par_o_impar = lambda num: num%2 == 0 
# print(par_o_impar(4))

# 7) 
# lista_numeros = []
# lista_cuadrados = []

# for i in range(1, N+1, 1):
#     lista_numeros.append(i)
#     lista_cuadrados.append(i**2)
# del lista_cuadrados[0:(len(lista_cuadrados)-10)]
# print(lista_cuadrados)

# 8) 
# lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
# lista2 = ["Martes", "Jueves"]
# lista_resultante =[]

# for i in lista:
#     if i not in lista2:
#         lista_resultante.append(i)
# print(lista)
# print(lista2)
# print(lista_resultante)

# 9) 
# numeros = [1,2,3]
# letras = ["c","b","a"]

# def ordenar(lista):
#     if sorted(lista) == lista :
#         return print(True)
#     else:
#         return print(False)

# ordenar(numeros)

# 10) 
# def cadena_capicua(cadena):
#     lista = []
#     listar =[]
#     for i in cadena:            
#         lista.append(i)
    
#     cadena = "".join(reversed(cadena))    #revierte la cadena
#     for i in cadena:
#         listar.append(i)
    
#     if lista == listar:
#         print("Es capicua")
#     else:
#         print("No es capicua")

# string = "Hola"

# cadena_capicua(string)

# 11) 
# cadena = input("Ingrese texto: " ,)
# cadena_cantrada=  cadena.center(80)
# print(cadena_cantrada)

# 12) 
# x = datetime.datetime(1990, 6, 10)
# def formato_fecha(tupla):
    
#     print(x.strftime("%d"), "of", x.strftime("%B"),"of", x.strftime("%Y") )

# formato_fecha(x)

# 13)
# frase = input("Ingrese frase: ")
# lista = []
# lista = frase.split(" ")
# conjunto = set()
# for i in lista:
#     conjunto.add(i)
# print("Conjunto: " , conjunto)
# print("Conjunto ordenado: " , sorted(conjunto, key=len)) 
# https://www.programiz.com/python-programming/methods/built-in/sorted
 
# 14) 
# dic = {'Borges':'Escritor','Lorca':'Escritor', 'Goya':'Pintor', 'Andric':'Escritor'}
# lista_claves = ['Lorca', 'Goya']
# def eliminar_claves(d,l):
#     eliminados =[]
#     for key in l: 
#             eliminados.append(key) 
#             del d[key]
#     if l == eliminados:
#         return print(True)
#     else:
#         return print(False)

# eliminar_claves(dic, lista_claves)

# https://www.geeksforgeeks.org/python-remove-multiple-keys-from-dictionary/

# 15) 
# cadena="una manzana dos manzanas tres manzanas cuatro manzanas"

# def eliminar_subcadena(c,pos, cant_c):
#     subcadena = c[pos:(pos+cant_c)]
#     print(subcadena)

# eliminar_subcadena(cadena,4, 40)






