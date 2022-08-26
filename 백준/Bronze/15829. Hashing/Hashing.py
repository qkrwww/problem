r=31
M=1234567891
L = int(input())
a= input()
b = 0
for i in range(L):
    b += (ord(a[i])-96) * (r ** i)
print(b % M)