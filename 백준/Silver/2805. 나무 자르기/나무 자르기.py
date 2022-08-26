N, M = map(int, input().split())
L= list(map(int, input().split()))
start, end = 1, max(L)
while start <= end:
    mid = (start+end) // 2
    log = 0 
    for i in L:
        if i >= mid:
            log += i - mid
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)