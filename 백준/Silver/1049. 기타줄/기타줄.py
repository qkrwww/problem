n, m = map(int, input().split())
P = []
S = []
for _ in range(m):
    a, b = map(int, input().split())
    P.append(a)
    S.append(b)
M = min(P)
c = 0
while n > 0:
    if n >= 6:
        N = min(S)*6
        n -= 6
    else:
        N = min(S)*n
        n -= n
    if N < M:
        c += N
    else:
        c += M
print(c)