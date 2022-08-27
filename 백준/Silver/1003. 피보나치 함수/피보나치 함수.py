z = [1, 0, 1]
o = [0, 1, 1]
def fibonacci(n):
    l = len(z)
    if n >= l:
        for i in range(l, n+1):
            z.append(z[i-1] + z[i-2])
            o.append(o[i-1] + o[i-2])
    print(f'{z[n]} {o[n]}')
T = int(input())  
for _ in range(T):
    fibonacci(int(input()))