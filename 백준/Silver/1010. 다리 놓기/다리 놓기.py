def n(a):
    b=1
    for i in range(1,a+1):
        b*=i
    return b
c=int(input())
for _ in range(c):
    d,e=map(int,input().split())
    f=n(e)/(n(d)*n(e-d))
    print(int(f))