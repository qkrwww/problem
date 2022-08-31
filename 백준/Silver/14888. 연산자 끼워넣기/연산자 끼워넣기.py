import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
L = list(map(int, input().split()))
max_mum = -1e9
min_mum = 1e9
def dfs(a, t, p, m, g, d):
    global max_mum, min_mum
    if a == N:
        max_mum = max(t, max_mum)
        min_mum = min(t, min_mum)
        return
    if p:
        dfs(a + 1, t + num[a], p - 1, m, g, d)
    if m:
        dfs(a + 1, t - num[a], p, m - 1, g, d)
    if g:
        dfs(a + 1, t * num[a], p, m, g - 1, d)
    if d:
        dfs(a + 1, int(t / num[a]), p, m, g, d - 1)
dfs(1, num[0], L[0], L[1], L[2], L[3])
print(max_mum)
print(min_mum)