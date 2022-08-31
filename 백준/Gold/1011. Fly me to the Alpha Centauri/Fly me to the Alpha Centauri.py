N=int(input())
for i in range(N):
    x, y = map(int, input().split())
    d = y - x
    c = 0
    m = 1
    s = 0
    while s < d:
        c += 1
        s += m
        if c % 2 == 0:
            m += 1
    print(c)