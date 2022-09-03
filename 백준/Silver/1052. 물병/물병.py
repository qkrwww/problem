n, k = map(int, input().split())
c = 0
while bin(n).count('1') > k:
    n = n+1
    c = c +1
print(c)