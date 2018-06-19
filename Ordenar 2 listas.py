#Se establece la existencia de ambas listas las cuales seran ingresadas por el usuario
lista_1= []
lista_2= []
#Además se establece la variable dato para poder ir ingresando datos a las tablas infinitamente
dato=0

#Se ingresan los datos para la primera lista
print("[Ingrese datos para la primera lista]\n")
#Repetirá este bucle hasta que el usuario presione ENTER
while str(dato)!="":
  dato=input("Presione ENTER para dejar de ingresar datos: ")
  if dato!=str():
    #Si el usuario ingresa un dato distinto a un número, va directo al except y establece la variable como 0 y no ingresa el dato a la lista
    try:
      lista_1.append(float(dato))
    except ValueError:
      dato=0
      
#Se restablece el valor de la variable dato a 0 para poder entrar al siguiente bucle de ingreso de datos    
dato=0

#Se ingresan los datos para la segunda lista
print("\n\n[Ingrese datos para la segunda lista]\n")
#Repetirá este bucle hasta que el usuario presione ENTER
while str(dato)!="":
  dato=input("Presione ENTER para dejar de ingresar datos: ")
  if dato!=str():
    #Si el usuario ingresa un dato distinto a un número, va directo al except y establece la variable como 0 y no ingresa el dato a la lista
    try:
      lista_2.append(float(dato))
    except ValueError:
      dato=0

#Se establece la función burbuja para ordenar los datos de las listas
def burbuja(lista):
  #Repetirá el siguiente bloque de codigo hasta que TODOS los números hayan sido ordenados completamente
  for i in range(1, len(lista)):
    #Leera todos los datos de la lista 1 por 1
    for j in range(0, len(lista)-i):
      #Comparará el elemento j con j+1
      if lista[j] > lista[j+1]:
        #Si el elemento j es mayor que el elemento j+1  estos cambiaran de posicion
        elemento = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = elemento

  return lista

print("\n################################################################################")

#Output de listas originales
print("\n[Listas originales]\n")
print("Lista 1: ")
print(lista_1)
print("\nLista 2: ")
print(lista_2)
print("\nLista combinada: ")
print(lista_1+lista_2)

print("\n################################################################################")

#Output de listas ordenadas de menor a mayor
print("\n[Listas ordenadas]\n")
print("Lista 1: ")
print(burbuja(lista_1))
print("\nLista 2: ")
print(burbuja(lista_2))
print("\nLista combinada: ")
print(burbuja(lista_1+lista_2))
