n, m = map(int, input().split())
s = list(map(int ,input().split()))
q = [i for i in range(1, n + 1)]
c = 0
for i in range(m):
    a = len(q)
    b = q.index(s[i])
    if b < a - b:
        while True:
            if q[0] == s[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                c += 1
    else:
        while True:
            if q[0] == s[i]:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                c += 1
print(c)