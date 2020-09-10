y=float(input())
x=int(y/1000)
t=1
while (x > 0):
    t = t*x
    x -= 2
k= t % 100
print(k)
