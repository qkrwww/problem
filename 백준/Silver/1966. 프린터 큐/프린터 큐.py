T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    L=list(map(int,input().split()))
    P=[]
    R=[]
    for j in range(N):
       P.append([j,L[j]])
    L.sort()
    while len(P)!=0:
        if P[0][1]==L[-1]:
            R.append(P.pop(0))
            L.pop()
        else:
            P.append(P.pop(0))
    for k in range(N):
        if R[k][0] == M:
            print(k+1)