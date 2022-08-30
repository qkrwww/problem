A,B=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
L=[]
L.extend(a)
L.extend(b)
L.sort()
for i in range(A+B):
    print(L[i],end=' ')