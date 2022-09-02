N = int(input())
L = [i for i in range(1, N+1)]
D = []

while len(L) != 1:
    D.append(L.pop(0))
    L.append(L.pop(0))

for i in D:
    print(i, end = ' ')
print(L[0])