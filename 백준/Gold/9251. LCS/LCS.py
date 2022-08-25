import sys
a=sys.stdin.readline().strip()
b=sys.stdin.readline().strip()
L=[0]*len(b)
for i in range(len(a)):
    num=0
    for j in range(len(b)):
        if num<L[j]:
            num=L[j]
        elif a[i]==b[j]:
            L[j]=num+1
print(max(L))