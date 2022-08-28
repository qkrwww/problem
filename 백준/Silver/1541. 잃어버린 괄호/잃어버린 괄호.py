a=input().split('-')
n=[]
for i in a:
    c=0
    s=i.split('+')
    for j in s:
        c+=int(j)
    n.append(c)
m=n[0]
for i in range(1,len(n)):
    m-=n[i]
print(m)