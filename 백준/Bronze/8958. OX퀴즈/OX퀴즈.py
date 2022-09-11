n=int(input())
for i in range(n):
    a=list(input())
    b=0
    c=1
    for j in a:
        if j=='O':
            b+=c
            c+=1
        else:
            c=1
    print(b)