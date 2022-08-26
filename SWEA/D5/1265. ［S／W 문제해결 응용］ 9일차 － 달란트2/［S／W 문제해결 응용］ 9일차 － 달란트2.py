T=int(input())
for i in range(1,T+1):
    N,M=map(int,input().split())
    a=N//M
    b=N%M
    c=1
    L=[]
    for j in range(M):
        L.append(a)
    for k in range(b):
        L[k] +=1
    for l in range(M):
        c *=L[l]
    print(f'#{i} {c}')