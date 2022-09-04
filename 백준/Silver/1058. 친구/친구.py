n = int(input())
s = []
v = [[0] * n for i in range(n)]
def f():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if s[i][j] == "Y" or (s[i][k] == "Y" and s[k][j] == "Y"):
                    v[i][j] = 1
for i in range(n):
    s.append(list(input().strip()))
f()
r = 0
for i in range(n):
    c = 0
    for j in range(n):
        if v[i][j] == 1:
            c += 1
    r = max(r, c)
print(r)