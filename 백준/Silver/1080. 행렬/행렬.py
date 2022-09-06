def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]
def check():
  for i in range(N):
    for j in range(M):
      if A[i][j] != B[i][j]:
        return False
  return True
N, M = map(int, input().split())
A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]
c = 0
for i in range(N-2):
  for j in range(M-2):
    if A[i][j] != B[i][j]:
        reverse(i, j)
        c += 1
if check():
    print(c)
else:
    print("-1")