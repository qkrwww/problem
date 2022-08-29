n=int(input())
t=[]
for i in range(n):
    a,b=map(int,input().split())
    t.append([a,b])
t=sorted(t,key=lambda x:x[0])
t=sorted(t,key=lambda x:x[1])
c=0
d=0
for i,j in t:
    if i>=c:
        d+=1
        c=j
print(d)