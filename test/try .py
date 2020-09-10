for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    k = list(map(int, input().split()))
    x = (a * -1) + b
    y = (c * -1) + d
    if  ((k[2] + k[0]) <= x and (k[4] + k[0]) >= x) and ((k[3] + k[1]) <= y and (k[5] + k[1]) >= y) :
         print("Yes")
         print(x)
         print(y)
    else:
        print("No")
        print(x)
        print(y)
