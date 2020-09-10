for i in range(int(input())):
    a, b = map(int, input().split())
    if a % b != 0:
        for i in range(b):
            if (a + (b-i)) % b == 0:
                print(b-i)
                break
    else: print(0)

