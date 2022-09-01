n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a%10==0:
        print(10)
    elif a%10==1:
        print(1)
    elif a%10==2:
        B=[6,2,4,8]
        print(B[b%4])
    elif a%10==3:
        B=[1,3,9,7]
        print(B[b%4])
    elif a%10==4:
        B=[6,4]
        print(B[b%2])
    elif a%10==5:
        print(5)
    elif a%10==6:
        print(6)
    elif a%10==7:
        B=[1,7,9,3]
        print(B[b%4])
    elif a%10==8:
        B=[6,8,4,2]
        print(B[b%4])
    elif a%10==9:
        B=[1,9]
        print(B[b%2])