a=int(input())
n=list(map(int,input().split()))
b=int(input())
m=list(map(int,input().split()))
n.sort()
for i in m:
    c=0
    d=a-1
    while c<=d:
        e=(c+d)//2
        if i ==n[e]:
            print(1)
            break
        elif i >n[e]:
            c=e+1
        elif i <n[e]:
            d=e-1
    if c>d:
        print(0)