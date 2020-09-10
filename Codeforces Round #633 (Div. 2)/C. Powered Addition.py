t=int(input())
def minimum_time(a,b):
	d=b-a
	i=1
	x=1
	if a==b:
	    return 0
	while (x<d):
		i+=1
		x=2**i-1
	return i
for i in range(t):
    n=int(input())
    lista=input().split()
    errors=[]
    difference=0
    for j in range(n):
        lista[j]=int(lista[j])
    j=0
    temp=lista[0]
    for i in range(n):
        if lista[i]>=temp:
            temp=lista[i]
        else:
            if temp-lista[i]>difference:
                difference=temp-lista[i]
    print(minimum_time(1,1+difference))