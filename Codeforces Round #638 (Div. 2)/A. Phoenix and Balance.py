s=[2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184]
for _ in range(int(input())):
    k=0
    p=int(input())
    if p % 2 != 0 :
        b=(p+1)/2
    else:
        b=p/2
    for i in range(p):
        k+=s[i]
    for i in range(0,int(b)):
        k-=2*s[i+int(b)-1]
    if k < 0:
        k*=-1
    print(k)


