for _ in range(int(input())):
    a,b = map(int, input().split())
    c= list (map(int, input().split()))
    d=sum(c)
    if d < b:
        print(d)
    else: print(b)