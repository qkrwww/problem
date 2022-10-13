N, M, B = map(int, input().split())
L = [ list(map(int, input().split())) for _ in range(N)]
H = [0 for _ in range(257)]
t = 100000001
h = 0
s = B 

for i in L:
    for j in i:
        H[j] += 1
        s += j

min_h = min([ min(i) for i in L ])
max_h = s // (M * N)

for l in range(min_h, max_h+1):
    cost = 0
    d = B
    for k in range(257):
        if h < k:
            cost += H[k] * abs(l - k) * 2
            d += H[k] * abs(l - k)
        else:
            cost += H[k] * abs(l - k)
            d -= H[k] * abs(l - k)
            
    if cost <= t and d >= 0:
        t = cost
        h = l

print(t, h)