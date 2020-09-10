for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    mid = (n - 1) // 2
    ans = []
    k = 0
    while 0 <= mid <= n - 1:
        ans.append(arr[mid])
        if k > 0:
            k = -k - 1
        else:
            k = -k + 1
        mid += k
    print(*ans)