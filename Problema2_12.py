SUE=int(input("Dame el sueldo del trabajador :"))
CATE=int(input("Dame la categoria del trabajador :"))
HE=int(input("Dame la horas extras que trabajo :"))
if CATE == 1:
    PHE = 30
if CATE == 2:
    PHE = 38
if CATE == 3:
    PHE = 50
if CATE == 4:
    PHE = 70
if CATE > 4:
        PHE = 0
if HE > 30:
    NSUE=SUE+30*PHE
else:
    NSUE=SUE+HE*PHE
print(f"El nuevo sueldo es {NSUE}")
print("Fin del programa")
