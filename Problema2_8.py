COMPRA=float(input("Valor de lo comprado: $"))
if COMPRA < 500:
    print(f"TOTAL A PAGAR{COMPRA}")
elif COMPRA<= 1000:
    PAGAR=COMPRA-(COMPRA*0.05)
    print(f"TOTAL A PAGAR :${PAGAR}")
elif COMPRA<= 7000:
    PAGAR=COMPRA-(COMPRA*0.11)
    print(f"TOTAL A PAGAR :${PAGAR}")
elif COMPRA<= 15000:
    PAGAR=COMPRA-(COMPRA*0.18)
    print(f"TOTAL A PAGAR :${PAGAR}")
else:
    PAGAR=COMPRA-(COMPRA*0.25)
    print(f"TOTAL A PAGAR :${PAGAR}")
print("Fin del programa")
