n=int(input())
L=[[0 for i in range(10)] for j in range(101)]
for i in range(1,10):
    L[1][i]=1
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            L[i][j]=L[i-1][1]
        elif j==9:
            L[i][j]=L[i-1][8]
        else:
            L[i][j]=L[i-1][j-1]+L[i-1][j+1]
print(sum(L[n])%1000000000)