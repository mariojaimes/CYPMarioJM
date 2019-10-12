SUE= float(input("Dame el sueldo del trabajador : $ "))
if SUE<1000:
    AUM= (SUE*0.15)
    NSUE= (SUE +AUM)
    print(f"Su nuevo sueldo sera ${NSUE}. ")
if SUE>1000:
    AUM= (SUE*0.12)
    NSUE= (SUE +AUM)
    print(f"Su nuevo sueldo sera ${NSUE}. ")
print( "Felicidades")
