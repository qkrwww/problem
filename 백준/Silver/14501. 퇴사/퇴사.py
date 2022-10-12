n=int(input())
t=[]
p=[]
L=[]
for i in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)
    L.append(b)
L.append(0)
for i in range(n-1,-1,-1):
    if t[i]+i>n:
        L[i]=L[i+1]
    else:
        L[i]=max(L[i+1],p[i]+L[i+t[i]])
print(L[0])