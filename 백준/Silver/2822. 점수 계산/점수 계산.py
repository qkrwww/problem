x=[]
for i in range(8):
    x.append(int(input()))
y=sorted(x,reverse=True)
y=y[0:5]
z=[]
for j in range(8):
    if x[j] in y:
        z.append(j+1)
print(sum(y))
for k in range(5):
    print(z[k],end=' ')
print()