n,r,c=map(int, input().split())
a=0
while n > 1:
    s=(2**n)//2
    if r<s and c<s:
        pass
    elif r<s and c>=s:
        a+=s**2
        c-=s
    elif r>=s and c<s:
        a+=2*s**2
        r-=s
    elif r>=s and c>=s:
        a+=3*s**2
        r-=s
        c-=s
    n-=1
if r==0 and c==0:
    print(a)
if r==0 and c==1:
    print(a+1)
if r==1 and c==0:
    print(a+2)
if r==1 and c==1:
    print(a+3)