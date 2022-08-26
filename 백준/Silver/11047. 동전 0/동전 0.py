N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(int(input()))
c=0
j=1
for j in reversed(range(N)):
    c+=M//L[j]
    M=M%L[j]
print(c)