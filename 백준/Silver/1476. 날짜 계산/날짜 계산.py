E,S,M=map(int,input().split())
e,s,m,y=1,1,1,1
while True:
    if E==e and S==s and M==m:
        break
    e+=1
    s+=1
    m+=1
    y+=1
    if e>15:
        e-=15
    if s>28:
        s-=28
    if m>19:
        m-=19
print(y)