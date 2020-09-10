n, m = map(int, input().split())
bry = []
ss = 0
fk = 0
fm = 0
a=0
for i in range(n):
    a, b = map(int, input().split())
    bry.append(a)
    bry.append(b)

for i in range(len(bry)):
    if i % 2 == 0:
        if bry[i] + bry[i + 1] == m:
            ss += 1
            bry[i]=0
            bry[i+1]=0
        if bry[i] + bry[i + 1] > m:
            if len(bry)<3:
                a=1
            else:
                kkm = bry[i + 1] - m
                if kkm < 0:
                    fk += bry[i] + kkm
                    ss += 1
                    bry[i] = 0
                    bry[i + 1] = 0
        if bry[i] >= m:
            ss += 1
            fk += (bry[i] - m)
        else:
            fk += bry[i]
    else:
        if bry[i] >= m:
            ss += 1
            fm += (bry[i] - m)
        else:
            fm += bry[i]
ss += int(fk / m)
ss += int(fm / m)
print(ss)




