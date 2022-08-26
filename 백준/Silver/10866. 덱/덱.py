import sys
from collections import deque
input=sys.stdin.readline
a = int(input())
s=deque()
for i in range(a):
    b=list(map(str, input().split()))
    if b[0]=='push_front':
        s.appendleft(b[1])
    elif b[0]=='push_back':
        s.append(b[1])    
    elif b[0]=='size':
        print(len(s))
    elif b[0]=='empty':
        if len(s)==0:
            print(1)
        else:
            print(0)
    elif b[0]=='pop_front':
        if len(s)==0:
            print(-1)
        else:
            print(int(s.popleft()))
    elif b[0]=='pop_back':
        if len(s)==0:
            print(-1)
        else:
            print(int(s.pop()))
    elif b[0]=='front':
        if len(s)==0:
            print(-1)
        else:
            print(int(s[0]))
    elif b[0]=='back':
        if len(s)==0:
            print(-1)
        else:
            print(s[-1])