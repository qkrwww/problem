n = int(input())
t = list(map(int, input().split()))
l = sorted(t)
L = []
for i in range(n):
    a = l.index(t[i])
    L.append(a)
    l[a] = -1
print(*L)