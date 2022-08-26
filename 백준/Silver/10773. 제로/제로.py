n=int(input())
l=[]
for _ in range(n):
    b=int(input())
    if b==0:
        l.pop()
    else:
        l.append(b)
print(sum(l))