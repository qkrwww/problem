A, B = map(str, input().split(' '))
c = 0
if len(A) != len(B):
    print(0)
else: 
    for i in range(len(A)):
        if A[i] == B[i]:
            if A[i] == '8':
                c += 1
        else:
            break
    print(c)