import sys
input=sys.stdin.readline
a = int(input())
s=[]
for i in range(a):
    b=list(map(str, input().split()))
    if b[0]=='push':
        s.append(b[1])
    elif b[0]=='top':
        if len(s)==0:
            print(-1)
        else:
            print(int(s[-1]))
    elif b[0]=='size':
        print(len(s))
    elif b[0]=='empty':
        if len(s)==0:
            print(1)
        else:
            print(0)
    elif b[0]=='pop':
        if len(s)==0:
            print(-1)
        else:
            print(int(s.pop()))