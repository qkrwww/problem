import sys
input = sys.stdin.readline
a=int(input())
l=[]
for _ in range(a):
    b,n=map(str,input().split())
    b=int(b)
    l.append((b,n))
l.sort(key=lambda c:(c[0]))
for c in l:
    print(c[0],c[1])