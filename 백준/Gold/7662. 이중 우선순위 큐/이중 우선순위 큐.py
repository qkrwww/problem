import sys
import heapq
T = int(input())
for _ in range(T):
    k = int(input())
    m = []
    n = []
    d = [0]*k
    for i in range(k):
        a, b = sys.stdin.readline().split()
        if a == 'I':
            heapq.heappush(m,((-1)*int(b),i))
            heapq.heappush(n,(int(b),i))
        elif a == 'D':
            if b == '-1':
                while n:
                    if d[n[0][1]] == 1:
                        heapq.heappop(n)
                    else:
                        break
                if n:
                    min = n[0][1]
                    d[min] = 1
                    heapq.heappop(n)
                    
            elif b == '1':
                while m:
                    if d[m[0][1]] == 1:
                        heapq.heappop(m)
                    else:
                        break
                if m:
                    max = m[0][1]
                    d[max] = 1
                    heapq.heappop(m)          
    while m:
            if d[m[0][1]] == 1:
                heapq.heappop(m)
            else:
                break
    while n:
            if d[n[0][1]] == 1:
                heapq.heappop(n)
            else:
                break
    if n:
        print((-1)*m[0][0], n[0][0])
    else:
        print("EMPTY")