N, M = map(int,input().split())
L = [list(input().strip()) for _ in range(N)]
a = -1
def R(S):
    S = int(S)
    return int(S ** 0.5) ** 2 == S
for i in range(N):
    for j in range(M):
        for k in range(-N,N):
            for l in range(-M,M):
                S = ""
                x,y = i,j
                if k == 0 and l == 0:
                    continue
                while 0 <= x < N and 0 <= y < M:
                    S += L[x][y]
                    if R(S):
                        a = max(a,int(S))
                    x += k
                    y += l
print(a)