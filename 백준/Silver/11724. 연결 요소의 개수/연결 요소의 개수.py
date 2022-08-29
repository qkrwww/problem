from collections import deque
import sys
input = sys.stdin.readline
def bfs(g, s, V):
    queue = deque([s])
    V[s] = True
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if not V[i]:
                queue.append(i)
                V[i] = True
N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
V = [False] * (N + 1)
for i in range(M):
    n, m = map(int, input().split())
    g[m].append(n)
    g[n].append(m)
c = 0
for i in range(1, N+1):
    if not V[i]:
        bfs(g, i, V)
        c += 1
print(c)