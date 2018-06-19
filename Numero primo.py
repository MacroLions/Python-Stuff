numero=int(input("Ingrese un número entero y mayor que 1: "))

while int(numero)<=1:
    numero=int(input("ingrese un número valido: "))

divisor=numero
divisores=0

for i in range(numero):
    resuido=int(int(numero)%int(divisor))
    
    if int(resuido)==0:
        divisores=divisores+1
    divisor=divisor-1

if int(divisores)>2:
    print("El número no es primo")

else:
    print("El número es primo")
    
    
    
