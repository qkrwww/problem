M,N=map(int,input().split())
L=[]
R=[]
for i in range(1,M+1):
    L.append(i)
while len(L) !=0:
    for j in range(N-1):
        L.append(L.pop(0))
    R.append(L.pop(0))
print('<',end='')
for k in range(M-1):
    print(f'{R[k]},', end=' ')
print(R[-1],end='')
print('>',end='')