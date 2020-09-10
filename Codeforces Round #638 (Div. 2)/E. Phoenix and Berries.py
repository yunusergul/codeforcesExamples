n,m=map(int,input().split())
bry=[]
ss=0
olm=[]
kfaz=[]
mfaz=[]
fk=0
fm=0
kkm=0
kkk=0
for i in range(n):
    a, b = map(int, input().split())
    bry.append(a)
    bry.append(b)

for i in range(len(bry)):
    if i%2==0:
            if bry[i]+bry[i+1] == m:
                ss += 1



            elif bry[i]+bry[i+1] > m:
                kkm=bry[i+1]-m
                kkk=bry[i]-m
                if len(bry) >3:
                    fk+=bry[i]
                    fm+=bry[i+1]
                else:
                    if  kkm < 0:
                        fk+=bry[i]-kkm
                        ss+=1


ss+=int(fk/m)
ss+=int(fm/m)

print(ss)
print("------------------------")
print(fk)
print(fm)



