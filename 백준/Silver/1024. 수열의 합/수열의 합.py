a,b=map(int,input().split())
z=-1
d=0
for i in range(b,101):
    c=(i*i-i)/2
    if (a-c)%i==0 and (a-c)//i>=0:
        z=(a-c)//i
        d=i
        break
if z==-1:
    print(-1)
else:
    for i in range(d):
        print(int(z+i))