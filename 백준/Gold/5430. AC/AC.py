import sys
from collections import deque
t = int(input())
for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    L = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(L)
    r, f, b = 0, 0, len(queue)-1
    G = 0
    if n == 0:
        queue = []
        f = 0
        b = 0
    for j in p:
        if j == 'R':
            r += 1
        elif j == 'D':
            if len(queue) < 1:
                G = 1
                print("error")
                break
            else:
                if r % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if G == 0:
        if r % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")