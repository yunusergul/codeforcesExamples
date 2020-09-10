from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


t = int(input())
for _ in range(t):
    n = int(input())
    print(1, n - 1)