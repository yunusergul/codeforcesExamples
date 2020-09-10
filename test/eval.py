t = eval(input())
for _ in range(t):
    n = eval(input())
    arr = [int(x) for x in input().split()]

    temp = set(arr)
    print(len(temp))