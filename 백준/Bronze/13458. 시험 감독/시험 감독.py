n=int(input())
s=list(map(int, input().split()))
b,c=map(int, input().split())
a=0
for i in s:
    i-=b
    r=1
    if i>0:
        r+=i//c
        if i%c!=0:
            r+=1
    a+=r
print(a)