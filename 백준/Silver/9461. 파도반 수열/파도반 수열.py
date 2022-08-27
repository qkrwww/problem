t=int(input())
P=[0 for _ in range(101)]
P[1]=1
P[2]=1
P[3]=1
for a in range(4,101):
    P[a]=P[a-3]+P[a-2]
for i in range(t):
    print(P[int(input())])