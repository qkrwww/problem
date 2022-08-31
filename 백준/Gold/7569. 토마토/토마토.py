import sys
from collections import deque
m,n,h = map(int,sys.stdin.readline().split())
L = []
queue = deque([])
for i in range(h):
    R = []
    for j in range(n):
        R.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if R[j][k]==1:
                queue.append([i,j,k])
    L.append(R)
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft()   
    for i in range(6):
        X = x+dx[i]
        Y = y+dy[i]
        Z = z+dz[i]
        if 0<=X<h and 0<=Y<n and 0<=Z<m and L[X][Y][Z]==0:
            queue.append([X,Y,Z])
            L[X][Y][Z] = L[x][y][z]+1         
flag = False
for i in L:
    for j in i:
        for k in j:
            if k == 0:
                flag = True
                break    
if flag:
    print(-1)
else:
    M = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                M = max(M,L[i][j][k])
    print(M-1)