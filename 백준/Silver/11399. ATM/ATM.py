N=int(input())
L=list(map(int,input().split()))
L.sort()
a=0
for i in range(N):
    a+=L[i]*(N-i)
print(a)