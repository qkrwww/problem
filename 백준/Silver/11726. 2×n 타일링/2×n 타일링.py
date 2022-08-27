s=[0,1,2]
n=int(input())
for i in range(3,n+3):
    s.append(s[i-2] + s[i-1])
print(s[n]%10007)