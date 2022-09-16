T=int(input())
for i in range(1,T+1):
    N=int(input())
    a=round(N**(1/3),2)
    if a%1 !=0:
        print(f'#{i} {-1}')
    else:
        print(F'#{i} {int(a)}')