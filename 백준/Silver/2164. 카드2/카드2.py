from collections import deque
deque=deque(range(1,int(input())+1))
for i in range(len(deque)-1):
    deque.popleft()
    b=deque.popleft()
    deque.append(b)
print(deque[0])
