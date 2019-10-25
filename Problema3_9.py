SERIE = 0
N = int(input("Numeros de enteros de la serie :"))
i = 1
for i in range (1,10,1):
    if i <= N:
        SERIE=SERIE + i**i
        i= i + 1
    else:
        print (f"{SERIE}")
print("Fin del programa")
