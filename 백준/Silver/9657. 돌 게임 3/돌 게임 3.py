N=int(input())
d=[0]*1001
d[1]=1
d[3]=1
d[4]=1
if N >4:
    for i in range(5,N+1):
        if not d[i-1]:
            d[i]=1
        if not d[i-3]:
            d[i]=1
        if not d[i-4]:
            d[i]=1
if d[N]==1:
    print('SK')
else:
    print('CY')