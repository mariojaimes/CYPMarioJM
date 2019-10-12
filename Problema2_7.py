A=int(input("Dame un numero entero: "))
B=int(input("Dame otro numero entero: "))
C=int(input("Dame otro numero entero: "))
if A<B:
    if B<C:
        print("Los numeros estan en orden creciente")
    else:
        print("Los numeros no estan en orden creciente")
else:
    print("Los numeros no estan en orden creciente")
print("Fin del programa")
