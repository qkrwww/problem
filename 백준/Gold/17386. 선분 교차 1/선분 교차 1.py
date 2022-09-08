import math
x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
if (x2-x1)!=0:
    a12=(y2-y1)/(x2-x1)
    b12=y1-(y2-y1)/(x2-x1)*x1
else:
    a12=1
    b12=x1
if (x4-x3)!=0:
    a34=(y4-y3)/(x4-x3)
    b34=y3-(y4-y3)/(x4-x3)*x3
else:
    a34=1
    b34=x3
if (x4-x3)!=0:
    D1=(a34*x1-y1+b34)/(math.sqrt(a34**2+1))
    D2=(a34*x2-y2+b34)/(math.sqrt(a34**2+1))
else:
    D1=x1-x3
    D2=x2-x3
if (x2-x1)!=0:
    D3=(a12*x3-y3+b12)/(math.sqrt(a12**2+1))
    D4=(a12*x4-y4+b12)/(math.sqrt(a12**2+1))
else:
    D3=x3-x2
    D4=x4-x2
if D1*D2<0 and D3*D4<0:
    print(1)
else:
    print(0)