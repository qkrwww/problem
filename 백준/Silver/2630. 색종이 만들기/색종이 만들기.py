N=int(input())
L=[list(map(int,input().split())) for _ in range(N)] 
r=[]
def s(x,y,N):
    c=L[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if c!=L[i][j]:
                s(x,y,N//2)
                s(x,y+N//2,N//2)
                s(x+N//2,y,N//2)
                s(x+N//2,y+N//2,N//2)
                return
    if c==0:
        r.append(0)
    else:
        r.append(1)
s(0,0,N)
print(r.count(0))
print(r.count(1))