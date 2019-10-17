MAT=int(input("Dame la matricula del alumno :"))
CARR=int(input("Carrera del alumno (0 Economia, 1 Computacion, 2 Contabilidad, 3 Administracion):"))
SEM=int(input("En que semestre esta :"))
PROM= float(input("Dame el promedio del alumno"))
if CARR==0:
    if SEM >= 6 and PROM>=8.8:
        print(f"El alumno conmatricula{MAT} incrito en {CARR} es aceptado")
if CARR==1:
    if SEM >= 6 and PROM>=8.5:
        print(f"El alumno conmatricula{MAT} incrito en {CARR} es aceptado")
if CARR==2:
    if SEM >= 5 and PROM>=8.5:
        print(f"El alumno conmatricula{MAT} incrito en {CARR} es aceptado")
if CARR==3:
    if SEM >= 5 and PROM>=8.5:
        print(f"El alumno conmatricula{MAT} incrito en {CARR} es aceptado")
print("Fin del programa")
