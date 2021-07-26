T = int(input())
cntA = 0
cntB = 0
cntC = 0
while T >= 10:
    if T >= 300:
        T -= 300
        cntA += 1
    elif T >= 60:
        T -= 60
        cntB += 1
    elif T >= 10:
        T -= 10
        cntC += 1
if T > 0:
    print(-1)
else:
    print(cntA,cntB,cntC) 
