MAY=-100000
MEN=100000
N=int(input("Dame un numero entero: "))
i=1
for i in range (1,14,1):
    if 1 >= N:
       NUM = int(input("Dame un numero: "))
        if NUM > MAY:
           MAY = NUM
        else:
            if NUM < MEN:
                MEN = NUM
else:
    i=i + 1
print(f"{MAY} , {NUM}")
