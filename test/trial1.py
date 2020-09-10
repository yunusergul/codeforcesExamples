def func(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[j] == arr[i] and j - i > 1):
                return 1

    return 0


t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    li = [int(i) for i in l]
    if (func(li, n)):
        print("YES")
    else:
        print("NO")