N=int(input())
a=b=1
for _ in range(N-2):
    a,b=b,a+b
print(b,N-2)