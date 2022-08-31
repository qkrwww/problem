import sys
input = sys.stdin.readline
n, m = map(int,input().rsplit())
a = []
for _ in range(n):
    r = list(map(int,input().rsplit()))
    a.append(r)
m, k = map(int,input().rsplit())
b = []
for _ in range(m):
    r = list(map(int,input().rsplit()))
    b.append(r)    
L = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for t in range(m):
            L[i][j] += a[i][t] * b[t][j]
for r in L:
    for l in r:
        print(l, end=" ")
    print()