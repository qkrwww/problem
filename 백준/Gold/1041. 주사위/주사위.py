n = int(input())
N = list(map(int, input().split()))
s=0
L=[]
if(n==1):
    N.sort()
    for i in range(0,5):
        s+=N[i]
else:
    L.append(min(N[0],N[5]))
    L.append(min(N[1],N[4]))
    L.append(min(N[2],N[3]))
    L.sort()
    m1 = L[0]
    m2 = L[0] + L[1]
    m3 = L[0] + L[1] + L[2]
    n1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    n2 = 4*(n-2) + 4*(n-1)
    n3 = 4
    s += n1 * m1
    s += n2 * m2
    s += n3 * m3
print(s)
