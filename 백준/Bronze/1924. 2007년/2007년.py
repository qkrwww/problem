a=['SUN','MON','TUE','WED','THU','FRI','SAT']
b=[31,28,31,30,31,30,31,31,30,31,30,31]
x,y=map(int,input().split())
d=0
for i in range(0,x-1):
    d+=b[i]
r=(d+y)%7
print(a[r])