T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    L=[list(map(int,input().split())) for _ in range(N)]
    num=0
    for i in range(N):
        a=0
        for j in range(M):
            if L[i][j]:
                a+=1
                if num <a:
                    num=a
            else:
                a=0
    for j in range(M):
        a=0
        for i in range(N):
            if L[i][j]:
                a+=1
                if num <a:
                    num=a
            else:
                a=0        
    print(f'#{t} {num}')