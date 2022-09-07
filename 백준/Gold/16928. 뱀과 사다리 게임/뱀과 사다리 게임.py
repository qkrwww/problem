from collections import deque
def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        t = queue.popleft()
        for i in range(1, 7):
            d = t + i
            if d > 100:
                continue
            c = L[d]
            if visited[c] == 0:
                queue.append(c)
                visited[c] = visited[t] + 1
                if c == 100:
                    return
n, m = map(int, input().split())
L = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, input().split())
    L[a] = b
visited = [0] * 101
bfs(1)
print(visited[100] - 1)