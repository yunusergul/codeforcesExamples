for _ in range(int(input())):
    n, m = map(int, input().split())
    if (n==1 and m>=1) or (m==1 and n>=1) or (n==m and n==2) :
        print("Yes")
    elif n == m and n>2:
        print("No")
