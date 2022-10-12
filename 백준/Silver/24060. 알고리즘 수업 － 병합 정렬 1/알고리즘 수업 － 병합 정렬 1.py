def merge_sort(L):
    if len(L)==1:
        return L
    m=(len(L)+1)//2
    l=merge_sort(L[:m])
    r=merge_sort(L[m:])
    i,j=0,0
    LL=[]
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            LL.append(l[i])
            R.append(l[i])
            i+=1
        else:
            LL.append(r[j])
            R.append(r[j])
            j+=1
    while i<len(l):
        LL.append(l[i])
        R.append(l[i])
        i+=1
    while j<len(r):
        LL.append(r[j])
        R.append(r[j])
        j+=1  
    return LL
n,k=map(int,input().split())
a=list(map(int,input().split()))
R=[]
merge_sort(a)
if len(R)>=k:
    print(R[k-1])
else:
    print(-1)