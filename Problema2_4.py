MAT=int(input("Dame una matricula de alumno: "))
CAL1=float(input("Dame la primera calificacion: "))
CAL2=float(input("Dame la segunda calificacion: "))
CAL3=float(input("Dame la tercera calificacion: "))
CAL4=float(input("Dame la cuarta calificacion: "))
CAL5=float(input("Dame la quinta calificacion: "))
PRO=(CAL1+CAL2+CAL3+CAL4+CAL5)/5
if PRO>=6:
    print(f"El alumno con matricula {MAT} tiene un promedio de {PRO} y esta APROBADO")
elif PRO<6:
    print(f"El alumno con matricula {MAT} tiene un promedio de {PRO} y esta REPROBADO")
print ("Fin del programa")
