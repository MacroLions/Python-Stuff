a=int(10)
binario = int(0)
cons = 1
while(a>=2):
    b = int(a%2)
    a = int(a/2)
    binario = binario + b*cons
    print("Ahora la constante vale "+str(cons))
    print("entonces el numero del residuo ")
    print("osea "+str(b)+" a la izquierda como 0 tenga")
    print("")
    cons = cons*10
    if(a==1):
        print("Este es el ultimo número, se moverá")
        print("Segun los valores de la ultima constante")
        print("Es decir "+str(cons))
        print("")
        binario = binario + a*cons

print(binario)
