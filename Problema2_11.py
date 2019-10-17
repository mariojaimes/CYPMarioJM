CLAVE=int(input("Dame la clave regional :"))
NUMIN=int(input("Cuantos minutos duro la llamada :"))
if CLAVE==12:
    COST=NUMIN*2
if CLAVE==15:
    COST=NUMIN*2.2
if CLAVE==18:
    COST=NUMIN*4.5
if CLAVE==19:
    COST=NUMIN*3.5
if CLAVE==23:
    COST=NUMIN*6
if CLAVE==25:
    COST=NUMIN*6
if CLAVE==29:
    COST=NUMIN*5
print(f"El costo total de la llamada fue ${COST}")
print("Fin del programa")
