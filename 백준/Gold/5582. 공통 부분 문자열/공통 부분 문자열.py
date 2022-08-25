a=input().strip()
b=input().strip()
L=[0]*(len(b)+1)
num=0
for i in range(len(a)):
    LL=[0]*(len(b)+1)
    for j in range(len(b)):
        if a[i] ==b[j]:
            LL[j+1]=L[j]+1
    num=max(num,max(LL))
    L=LL[:]
print(num)