MAT=int(input("Dame la matricula del alumno :"))
CARR=input("Carrera del alumno  
1=Economia,
2=Computacion,
3=contabilidad,
4=Administracion :")
SEM=int(input("En que semestre esta :"))
if CARR==1:
    if SEM >= 6 and PROM>=8.8:
        print(f"El alumno conmatricula{MAT} incrito en {CARR} es aceptado")
if CARR==2:
    if SEM >= 6 and PROM>=8.5:
        print(f"El alumno conmatricula{MAT} incrito en {CARR} es aceptado")
if CARR==3:
    if SEM >= 5 and PROM>=8.5:
        print(f"El alumno conmatricula{MAT} incrito en {CARR} es aceptado")
if CARR==4:
    if SEM >= 5 and PROM>=8.5:
        print(f"El alumno conmatricula{MAT} incrito en {CARR} es aceptado")
print("Fin del programa")
