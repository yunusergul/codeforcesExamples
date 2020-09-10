for i in range(int(input())):
    a,b,c,n = map(int,input().split())
    yt = (a + b + c + n)
    yy = ((-2)*a+b+c+n)
    r = yy % 3
    A = yy // 3
    B = a-b+A
    C = b-c+B
    print(yt)
    print(yy)
    print(r)
    print(A)
    print(B)
    print(C)
    print('YES'if r == 0 and A>=0 and B>=0 and C>=0 else 'NO')