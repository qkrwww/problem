import sys
n=int(sys.stdin.readline())
L=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    L.append([b,a])
L.sort()
for j in L:
    print(j[1],j[0])