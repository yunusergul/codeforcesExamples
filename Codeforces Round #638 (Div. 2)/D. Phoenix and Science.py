n = int(input())
while n > 0:
    n = n - 1
    l = []
    s = 0
    m = int(input())
    i = 1
    while i <= m:
        if s + i <= m:
            s += i
            l.append(i)
        i *= 2
    if s < m:
        l.append(m - s)
    l1 = sorted(l)

    print(len(l1) - 1)
    for j in range(1, len(l1)):
        print(l1[j] - l1[j - 1], end=" ")
    print()