from collections import deque
m,n = map(int,input().split())
L = []
for _ in range(n):
    L.append(list(map(int,input().split())))
queue = deque()
for i in range(n):
    for j in range(m):
        if L[i][j] == 1:
            queue.append((i,j))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
while queue:
    x,y = queue.popleft()
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0<=X<n and 0<=Y<m:
            if L[X][Y] == -1:
                continue
            if L[X][Y] == 0:
                queue.append((X,Y))
                L[X][Y] = L[x][y]+1
flag = False
for i in range(n):
    for j in range(m):
        if L[i][j] == 0:
            flag = True
            break
if flag:
    print(-1)
else:
    print(max(map(max,L))-1)