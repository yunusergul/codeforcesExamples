n=int(input())
m = str(input())
l=list(m.strip())
s=0
v=0
d=0
p=0
ss=0
for i in l:
    if s==0:
        ss+=1


    if s>=1:  ss-=1
    if s<0: v=1


    if i =="U": s+=1
    else: s-=1
print(ss)







