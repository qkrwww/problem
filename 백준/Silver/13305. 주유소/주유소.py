N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = b[0]
d = 0
for i in range(N-1):
    if c > b[i]:
        c = b[i]
    d += (c * a[i])
print(d)