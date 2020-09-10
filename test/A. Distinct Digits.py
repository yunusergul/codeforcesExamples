a,b = map(int,input().split())
p="-1"
for s in range(a,b+1):
    list = [x for x in str(s)]
    list2=[]
    for e in list:
        if e not in list2:
            list2.append(e)
    if len(list2) == len(list):
        p=str(s)
        break
print(p)





