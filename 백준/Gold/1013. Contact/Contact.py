import sys
import re
n = int(sys.stdin.readline())
for _ in range(n):
    t = str(sys.stdin.readline().rstrip("\n"))
    pattern = re.compile('(100+1+|01)+')
    res = pattern.fullmatch(t)
    if res:
        print('YES')
    else:
        print('NO')