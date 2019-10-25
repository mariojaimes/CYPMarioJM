SUMOTR=0
SUMPOS=0
CUEPOS=0
N=int(input("Dame un numero: "))
i=1
if i in range( 1,23,1):
    NUM=int(input("Dame un numero: "))
    if num > 0:
        SUMPOS = SUMPOS + NUM
        CUEPOS = CUEPOS + 1
    else:
        SUMOTR = SUMOTR + NUM
    i = i + 1
else:
    PROGEN = (SUMPOS + SUMOTR)/N
    PROPOS = (SUMPOS / CUEPOS)
print (f"{CUEPOS} , {PROPOS} ,{PROGEN}.")
