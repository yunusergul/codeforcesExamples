t = int(input())
for i in range(0, t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    b = True
    c = True
    for j in range(1, len(a)):
        if (a[j] - a[j - 1]) % 2 == 0:
            b = True
        elif (a[j] - a[j - 1]) % 2 != 0:
            b = False
            break
    if b:
        print("YES")
    elif not b:
        print("NO")