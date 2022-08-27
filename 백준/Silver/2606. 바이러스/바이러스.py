n = int(input())
m = int(input())
L = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    L[a].append(b)
    L[b].append(a)   
c = 0
v = [0]*(n+1)
def dfs(s):
    global c
    v[s] = 1
    for i in L[s]:
        if v[i]==0:
            dfs(i)
            c +=1
dfs(1)
print(c)