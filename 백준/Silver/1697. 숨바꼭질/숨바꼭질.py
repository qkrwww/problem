from collections import deque
def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            print(L[x])
            break

        for j in (x-1,x+1,x*2):
            if 0<=j<=m and not L[j]:
                L[j]=L[x]+1
                q.append(j)
n,k=map(int,input().split())
m=100000
L=[0]*(m+1)
bfs()