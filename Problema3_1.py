sumpar = 0
sumimp = 0
cuepar = 0
for i in range(1,271,2):
    num = float(input("Ingresa el sueldo del trabajador"))
    if num < i >0:
        if (-1 ** num) > 0:
            sumpar += num + cuepar # sumpar = sumpar + num + cuepar
        else:
            sumimp += num # sumimp = sumimp + num
    propar = sumpar / cuepar # propar = sumpar / cuepar
print("{probar}, {sumimp}")
