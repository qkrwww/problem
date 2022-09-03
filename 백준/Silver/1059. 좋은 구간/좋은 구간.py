L = int(input())
n = list(map(int, input().split()))
t = int(input())
n.append(0)
n.sort()
A = 0
for i in range(len(n)-1) :
    if n[i] == t or n[i+1] == t:
        A = 0
        break
    elif n[i] < t and t < n[i+1]:
        A = (t - n[i]) * (n[i+1] - t) - 1
        break
print(A)