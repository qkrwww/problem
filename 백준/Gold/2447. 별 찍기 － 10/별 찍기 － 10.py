def a(n):
  if n==1:
    return ['*']
  b=a(n//3)
  L=[]
  for i in b:
    L.append(i*3)
  for i in b:
    L.append(i+' '*(n//3)+i)
  for i in b:
    L.append(i*3)
  return L
N=int(input())
print('\n'.join(a(N)))