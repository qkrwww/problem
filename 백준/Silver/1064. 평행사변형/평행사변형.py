ax, ay, bx, by, cx, cy = map(int, input().split())
if ((ax-bx)*(ay-cy)==(ay-by)*(ax-cx)):
    print(-1.0)
else:
    A = ((ax-bx)**2 + (ay-by)**2)**0.5
    B = ((ax-cx)**2 + (ay-cy)**2)**0.5
    C = ((bx-cx)**2 + (by-cy)**2)**0.5
    l = [A+B, A+C, B+C]
    c = max(l) - min(l)
    print(2*c)