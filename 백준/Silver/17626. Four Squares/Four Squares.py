n = int(input())
m = 4
for a in range(int(n**0.5), int((n//4)**0.5), -1):
    if a*a == n:
        m = 1
        break
    else:
        x = n - a*a
        for b in range(int(x**0.5), int((x//3)**0.5), -1):
            if a*a + b*b == n:
                m = min(m, 2)
                continue
            else:
                x = n - a*a - b*b
                for c in range(int(x**0.5), int((x//2)**0.5), -1):
                    if n == a*a + b*b + c*c:
                        m = min(m, 3)
print(m)