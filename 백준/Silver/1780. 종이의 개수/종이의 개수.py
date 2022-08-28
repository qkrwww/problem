N =int(input())
L=[list(map(int,input().split())) for _ in range(N)]
a=0
b=0
c=0
def C(x,y,n):
    global a,b,c
    m=L[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if(L[i][j]!=m):
                for k in range(3):
                    for l in range(3):
                        C(x+k*n//3,y+l*n//3,n//3)
                return
    if(m==-1):
        a+=1
    elif(m==0):
        b+=1
    else:
        c+=1
C(0,0,N)
print(f'{a}\n{b}\n{c}')