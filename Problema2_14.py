TIPOENF=int(input("Que tipo de enfermadad es :"))
EDAD=int(input("Edad del enfermo :"))
DIAS=int(input("Dias que tiene enfermo :"))
if TIPOENF==1:
    COSTOT=DIAS*25
elif TIPOENF==2:
    COSTOT=DIAS*16
elif TIPOENF==3:
    COSTOT=DIAS*20
elif TIPOENF==4:
    COSTOT=DIAS*32
if EDAD >= 14 and EDAD<=22:
    COSTOT=COSTOT*1.10
print(f"EL costo total es de ${COSTOT}")
print("Fin del programa")
