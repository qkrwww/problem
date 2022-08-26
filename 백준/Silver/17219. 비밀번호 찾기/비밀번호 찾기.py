N,M=map(int,input().split())
L = {}
for _ in range(N):
    X, Y = input().split()
    L[X] = Y
for _ in range(M):
    print(L[input().rstrip()])