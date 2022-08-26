while True:
    b = input()
    L=[]
    if b =='.':
        break
    a=True
    for i in b:
        if i == '(':
            L.append(i)
        elif i == ')':
            if not L or L[-1] =='[':
                a=False
                break
            elif L[-1] == '(':
                L.pop()
        if i == '[':
            L.append(i)
        elif i == ']':
            if not L or L[-1] =='(':
                a=False
                break
            elif L[-1] =='[':
                L.pop()
    if a ==True and not L:
        print('yes')
    else:
        print('no')