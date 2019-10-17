PREBAS=float(input("Precio de lo comprado:$"))
if PREBAS > 500:
    IMP=20*0.30+(PREBAS-40)*0.50
elif PREBAS > 40:
    IMP=20*0.30+(PREBAS-40)*0.40
elif PREBAS > 20:
    IMP=(PREBAS-20)*0.30
else:
    IMP=0
PRETOT= PREBAS + IMP
print(f"EL objeto vale ${PREBAS} y con impuesto su valor es ${PRETOT}")
print("Fin del programa")
