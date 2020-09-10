n=int((input()))
mylist = [int(n) for n in input().split()]
ylist=[]
s=0
for m in mylist:
    if m not in ylist:
        ylist.append(m)
s=len(ylist)

for i in ylist:
    n = mylist.count(i)
    s+= (n-(n %2))/2
print(int(s))