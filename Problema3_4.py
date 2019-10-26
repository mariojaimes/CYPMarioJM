NOM=0
SUE=float(input("Dame el sueldo del trabajador: "))
for i in range (1,11,1):
    if SUE <> -1:
        if SUE < 1000:
        NSUE= SUE*1.15
        else:
        NSUE=SUE*1.12
    NOM=NOM+NSUE
    print(f"El nuevo sueldo es {NSUE}")
    else:
        print(f"{NOM}")
print("Fin del programa"
