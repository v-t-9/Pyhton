# 4)
# while True:
#     try:
#         num = int(input("Ingrese un numero divisor: " ,))
#         print("El resultado es: " , 10/num)
#         break
#     except ZeroDivisionError:
#         print("No se puede dividir por 0. Intente de nuevo")


# 5)

elementos = [1, 5, -2]
e = -2
def agregar_una_vez(lista, el):
        if el in lista:
            raise ValueError("Error: Imposible añadir elementos duplicados =>" , el)
        else:
              lista.append(el)
              print(lista)
    
agregar_una_vez(elementos,e)

