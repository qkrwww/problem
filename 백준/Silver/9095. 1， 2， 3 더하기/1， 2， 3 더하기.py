t=int(input())
def s(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return s(n-3)+s(n-2)+s(n-1)
for i in range(t):
    print(s(int(input())))