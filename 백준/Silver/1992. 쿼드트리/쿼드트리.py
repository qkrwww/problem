N=int(input())
L=[list(map(int,input().strip())) for _ in range(N)]
def d(x,y,n):
    c=L[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if c!=L[i][j]:
                c=-1
                break
    if c==-1:
        print('(',end='')
        n=n//2
        d(x,y,n)
        d(x,y+n,n)
        d(x+n,y,n)
        d(x+n,y+n,n)
        print(')',end='')
    elif c==1:
        print('1',end='')
    else:
        print('0',end='')
d(0,0,N)