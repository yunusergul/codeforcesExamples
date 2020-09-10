
t = [int(i) for i in input().split()]
p=[]
s=0
for k in range(t-1):
    if k in p:
        s+=1

    else:
        p.append(k)

for _ in range(int(input())):
    n, x = map(int, input().split())
    t = [int(i) for i in input().split()]
    sn=1
    for y in range(1,len(t)-2):
        if x<t[y]:
            sn=t[y]
            break
    if max(t)==min(t):
        sn=max(t)+1
    print(sn)