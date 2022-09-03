n, m, i = map(int, input().split())
c = 0
while m != i:
    m -= m // 2
    i -= i // 2
    c += 1
print(c)