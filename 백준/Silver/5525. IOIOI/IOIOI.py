N = int(input())
M = int(input())
S = input()
a, i, c = 0, 0, 0
while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        c += 1
        if c == N:
            a += 1
            c -= 1
    else:
        i += 1
        c = 0
print(a)