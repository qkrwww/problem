n, m = map(int, input().split())
l = [list(map(int ,input().strip())) for _ in range(n)]
a = []
for i in range(n):
    for j in range(m):
        b = l[i][j] 
        for k in range(j, m):
            if l[i][k] == b and i + k - j < n and k < m:
                if l[i + k - j][j] == b and l[i + k - j][k] == b:
                    a.append((k - j + 1) ** 2)
print(max(a))