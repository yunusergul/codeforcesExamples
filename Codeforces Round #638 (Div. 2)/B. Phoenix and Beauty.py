t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=[]
    s=set(map(int,input().split()))
    if(len(s)>k):
        print(-1)
    else:
        print(n*k)
        for j in range(n):
            for p in s:
                arr.append(p)
            for p in range(k-len(s)):
                arr.append(1)
        print(*arr,sep=" ")