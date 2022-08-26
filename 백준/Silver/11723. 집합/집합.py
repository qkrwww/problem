import sys
N = int(sys.stdin.readline())
S = set()
for _ in range(N):
    L = sys.stdin.readline().strip().split()
   
    if len(L) == 1:
        if L[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()  
    else:
        func, x = L[0], L[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)