N=int(input())
L=list(map(int, input().split()))
L=list(set(L))
L.sort()
for i in range(len(L)):
    print(L[i], end=' ')