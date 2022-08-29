n = int(input())
l = []
max_num = [(0,0),(0,0)]
for i in range(6):
    d,w = map(int,input().split())
    d = 0 if d<=2 else 1
    if w > max_num[d][1]:
        max_num[d] = (i,w)
    l.append((d,w))
ans = max_num[0][1]*max_num[1][1]
check = [False]*6
for idx,_ in max_num:
    for i in idx,(idx+1)%6,idx-1:
        check[i] = True
min_num = 1
for i in range(6):
    if not check[i]:
        min_num *= l[i][1]
print((ans-min_num)*n)