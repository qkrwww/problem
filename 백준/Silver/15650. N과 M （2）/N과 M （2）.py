n, m = map(int, input().split())
s=[]
def f(l):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(l, n + 1):
    if i not in s:
        s.append(i)
        f(i+1)
        s.pop()
f(1)
